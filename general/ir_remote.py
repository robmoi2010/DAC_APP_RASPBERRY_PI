import pigpio
import time
import configs.app_config as app_config
import dac.dac_volume as dac_volume
from dac.dac_volume import VOL_DIRECTION
from enum import Enum
from ui.remote_navigation import RemoteNavigation

remoteNav = RemoteNavigation()

config = app_config.getConfig()
irConfig = config["IR_REMOTE"]["BUTTON_HASH"]
BUTTON = Enum("BUTTON", irConfig)

buttonHash = [x for x in irConfig]

# Configuration
IR_GPIO = config["GPIO"]["PIN_MAP"][
    "IR_SENSOR"
]  # GPIO pin where the IR receiver is connected

# Initialize pigpio
pi = pigpio.pi()
if not pi.connected:
    exit()

# Globals
last_tick = 0
code = []
gap_timeout = 5000  # Microseconds; adjust if necessary


def decode_pulse(pulses):
    """Decodes the list of pulses into a hex code."""
    binary_code = ""
    for pulse in pulses:
        if pulse > 1000:  # Long pulses are '1's, short pulses are '0's
            binary_code += "1"
        else:
            binary_code += "0"

    if len(binary_code) % 8 == 0:
        hex_code = f"{int(binary_code, 2):X}"
        return hex_code
    return None


def ir_callback(gpio, level, tick):
    """Callback function to handle IR signals."""
    global last_tick, code

    if level == pigpio.TIMEOUT:
        if len(code) > 0:
            decoded = decode_pulse(code)
            if decoded:
                btn = next((k for k, v in irConfig.items() if v == decoded), None)
                handleRemoteButton(btn)
                print(f"Key Pressed: {btn} (Hex: {decoded})")
            code = []
    else:
        if last_tick != 0:
            pulse_len = pigpio.tickDiff(last_tick, tick)
            code.append(pulse_len)
        last_tick = tick

    # Set watchdog to detect end of signal
    pi.set_watchdog(IR_GPIO, 15)


# Setup GPIO
pi.set_mode(IR_GPIO, pigpio.INPUT)
pi.callback(IR_GPIO, pigpio.EITHER_EDGE, ir_callback)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting...")


def handleRemoteButton(button):
    if button == BUTTON.VOL_UP:
        dac_volume.updateVolume(VOL_DIRECTION.UP)
    elif button == BUTTON.VOL_DOWN:
        dac_volume.updateVolume(VOL_DIRECTION.DOWN)
    elif button == BUTTON.POWER:
        pass
    elif button == BUTTON.MUTE:
        dac_volume.muteUnmuteDac()
    elif button == BUTTON.UP:
        remoteNav.handle_up_button()
    elif button == BUTTON.DOWN:
        remoteNav.handle_down_button()
    elif button == BUTTON.OK:
        remoteNav.handle_OK_button()
