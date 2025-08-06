import asyncio
import pigpio
import time
from configs.app_config import Config
from enum import Enum
from system.ir_remote_router import IrRemoteRouter
from system.system_util import BUTTON

"""put functionality in a class and create a background thread to listen for ir remote signals during implementaion."""
"""create a function to capture and store ir codes. Put the ir codes in the config buttonhash array in order for the application to be used with any preconfigured remote."""
ir_remote_router 
config = Config().config
irConfig = config["IR_REMOTE"]["BUTTON_HASH"]

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


async def ir_callback(gpio, level, tick, ir_remote_router ):
    """Callback function to handle IR signals."""
    global last_tick, code

    if level == pigpio.TIMEOUT:
        if len(code) > 0:
            decoded = decode_pulse(code)
            if decoded:
                btn = {k for k, v in irConfig.items() if decoded in v}
                await ir_remote_router.handle_remote_button(map_button_name(btn))
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


def map_button_name(btn: str) -> BUTTON:
    if btn == "VOLUME_UP":
        return BUTTON.VOLUME_UP
    elif btn == "VOLUME_DOWN":
        return BUTTON.VOLUME_DOWN
    elif btn == "POWER":
        return BUTTON.POWER
    elif btn == "MUTE":
        return BUTTON.MUTE
    elif btn == "UP":
        return BUTTON.UP
    elif btn == "DOWN":
        return BUTTON.DOWN
    elif btn == "LEFT":
        return BUTTON.LEFT
    elif btn == "RIGHT":
        return BUTTON.RIGHT
    elif btn == "OK":
        return BUTTON.OK
