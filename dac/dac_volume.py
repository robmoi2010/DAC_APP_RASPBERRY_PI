import repo.storage as storage
import configs.app_config as app_config
import util.communication as communication
import volume.system_volume as volume


DAC_MIN_VOL = 255
DAC_MAX_VOL = 0
LOG_CURVE = 6
config = app_config.getConfig()

addrConfig = config["DAC"]["ADDR"]


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


def set_volume(volume):
    # hold both channels
    # communication.write(addrConfig["I2C_ADDR"], addrConfig["VOLUME_HOLD"], 1)
    # update volume of both channels
    communication.write(addrConfig["I2C_ADDR"], addrConfig["VOLUME_CH1"], volume)
    communication.write(addrConfig["I2C_ADDR"], addrConfig["VOLUME_CH2"], volume)
    # release hold on both channels


def update_volume(direction):
    currVol = volume.getCurrentVolume()
    steps = config["DAC"]["VOLUME"]["VOLUME_STEPS"]  # get volume steps from config
    if direction == volume.VOL_DIRECTION.UP:  # volume increase
        if currVol <= DAC_MAX_VOL:  # skip processing if volume is already at Max
            return
        currVol -= steps  # dacs lower value=increase

    else:
        if currVol >= DAC_MIN_VOL:  # skip processing if volume is already at Minimum
            return
        currVol += steps  # dacs higher value=decrease

    # currVol = getLogarithmicVolumeLevel(currVol)  # change from linear to logarithmic
    set_volume(currVol)
    volume.persistVolume(currVol)
    # update ui with the new volume
    volume.update_ui_volume(currVol)


def is_volume_disabled():
    return storage.read("DISABLE_VOLUME")


def disable_enable_volume():
    curr = storage.read("DISABLE_VOLUME")
    if curr == 0:
        set_volume(DAC_MAX_VOL)  # disable volume
        storage.write("DISABLE_VOLUME", 1)
        return 0  # disabled
    else:
        set_volume(volume.getCurrentVolume())
        storage.write("DISABLE_VOLUME", 0)
        return 1  # enabled


def mute_dac():
    communication.write(addrConfig["I2C_ADDR"], addrConfig["DAC_MUTE"], 3)


def unmute_dac():
    communication.write(addrConfig["I2C_ADDR"], addrConfig["DAC_MUTE"], 0)


def mute():
    muted = storage.read("DAC_MUTED")
    if muted == 1:
        unmute_dac()
        storage.write("DAC_MUTED", 0)
    else:
        mute_dac()
        storage.write("DAC_MUTED", 1)


def get_percentage_volume(volume):
    val = volume.map_value(volume, DAC_MIN_VOL, DAC_MAX_VOL, 0, 100)
    return int(val)


