import repo.storage as storage
import configs.app_config as app_config
import util.communication as communication
import volume.system_volume as volume
from volume.system_volume import VOLUME_ALGORITHM


DAC_MIN_VOL = 255
DAC_MAX_VOL = 0
LOG_CURVE = 6
config = app_config.getConfig()

addrConfig = config["DAC"]["ADDR"]
DAC_I2C_ADDR = addrConfig["I2C_ADDR"]

# def onkeyLeft(counter):
#     from ui.app import current_visible_frame

#     children = current_visible_frame.winfo_children()
#     print(counter)
#     children[counter].tk_focusPrev().focus_set()
#     return len(children)


# def onEnter(counter):
#     from ui.app import current_visible_frame

#     children = current_visible_frame.winfo_children()
#     print(counter)
#     children[counter].invoke()


# def onKeyRight(counter):
#     from ui.app import current_visible_frame

#     children = current_visible_frame.winfo_children()

#     children[counter].tk_focusNext().focus_set()
#     return len(children)


def set_volume(vol):
    # if logarithmic is set adjust volume to logarithmic scale
    if volume.get_current_volume_algorithm() == VOLUME_ALGORITHM.LOGARITHMIC:  
        vol = volume.get_logarithmic_volume_level(vol, DAC_MIN_VOL, DAC_MAX_VOL)
        print("vol:" + str(vol))
    # hold both channels
    hold_addr = addrConfig["DAC_SPDIF_SEL_ADDR"]
    hold_mask = 0b00001000
    data = communication.read(DAC_I2C_ADDR, hold_addr)
    data = data | hold_mask
    communication.write(DAC_I2C_ADDR, hold_addr, data)

    # update volume of both channels
    volume_1_addr = addrConfig["VOLUME_CH1"]
    volume_2_addr = addrConfig["VOLUME_CH2"]
    volume_data = format(vol, "08b")
    communication.write(DAC_I2C_ADDR, volume_1_addr, volume_data)
    communication.write(DAC_I2C_ADDR, volume_2_addr, volume_data)

    # release hold on both channels
    data = data & ~hold_mask
    communication.write(DAC_I2C_ADDR, hold_addr, data)


def update_volume(direction):
    currVol = volume.get_current_volume()
    steps = config["DAC"]["VOLUME"]["VOLUME_STEPS"]  # get volume steps from config
    if direction == volume.VOL_DIRECTION.UP:  # volume increase
        if currVol <= DAC_MAX_VOL:  # skip processing if volume is already at Max
            return
        currVol -= steps  # dacs lower value=increase
    else:
        if currVol >= DAC_MIN_VOL:  # skip processing if volume is already at Minimum
            return
        currVol += steps  # dacs higher value=decrease
    set_volume(currVol)
    volume.persist_volume(currVol)
    # update ui with the new volume
    volume.update_ui_volume(currVol)


def is_volume_disabled():
    return storage.read("DISABLE_VOLUME")


def disable_enable_volume(selected):
    curr = storage.read("DISABLE_VOLUME")
    if (curr == 0 and selected == 0) or (curr == 1 and selected == 1):
        return
    if selected == 1:
        set_volume(DAC_MAX_VOL)  # disable volume
        storage.write("DISABLE_VOLUME", 1)
        return 0  # disabled
    else:
        set_volume(volume.get_current_volume())
        storage.write("DISABLE_VOLUME", 0)
        return 1  # enabled


def mute_dac():
    mute_addr = addrConfig["DAC_MUTE"]
    mute_mask = 0b00000011
    data = communication.read(DAC_I2C_ADDR, mute_addr)
    data = data | mute_mask
    communication.write(DAC_I2C_ADDR, mute_addr, data)


def unmute_dac():
    mute_addr = addrConfig["DAC_MUTE"]
    mute_mask = 0b00000011
    data = communication.read(DAC_I2C_ADDR, mute_addr)
    data = data & ~mute_mask
    communication.write(DAC_I2C_ADDR, mute_addr, data)


def mute():
    muted = storage.read("DAC_MUTED")
    if muted == 1:
        unmute_dac()
        storage.write("DAC_MUTED", 0)
    else:
        mute_dac()
        storage.write("DAC_MUTED", 1)


def get_percentage_volume(vol):
    val = volume.map_value(vol, DAC_MIN_VOL, DAC_MAX_VOL, 0, 100)
    return int(val)
