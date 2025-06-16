import pigpio
import time
import configs.app_config as app_config
from enum import Enum
from registry.register import get_instance
from system.ir_remote_router import IrRemoteRouter

ir_remote_router: IrRemoteRouter = get_instance("irremoterouter")
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
                ir_remote_router.handle_remote_button(btn)
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
