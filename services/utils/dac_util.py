from dac import dac_filters
from model.model import ResponseModel
from services.utils.system_util import is_selected
from system import volume_encoder
import dac.ess_dac as dac

def create_filter_response():
    # 0 Minimum phase
    # 1 Linear phase apodizing first roll-off
    # 2 Linear phase fast roll-off
    # 3 Linear phase slow roll-off low ripple
    # 4 Linear phase slow roll-off
    # 5 Minimum phase fast roll-off
    # 6 Minimum phase slow roll-off
    # 7 Minimum phase slow roll-off low dispersion
    current_filter = dac_filters.get_current_filter()
    list = []
    r0 = ResponseModel(
        key="0", value="" + is_selected(current_filter, 0), display_name="Minimum phase"
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value="" + is_selected(current_filter, 1),
        display_name="Linear phase apodizing first roll-off",
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2",
        value="" + is_selected(current_filter, 2),
        display_name="Linear phase fast roll-off",
    )
    list.append(r2)
    r3 = ResponseModel(
        key="3",
        value="" + is_selected(current_filter, 3),
        display_name="Linear phase slow roll-off low ripple",
    )
    list.append(r3)
    r4 = ResponseModel(
        key="4",
        value="" + is_selected(current_filter, 4),
        display_name="Linear phase slow roll-off",
    )
    list.append(r4)
    r5 = ResponseModel(
        key="5",
        value="" + is_selected(current_filter, 5),
        display_name="Minimum phase fast roll-off",
    )
    list.append(r5)
    r6 = ResponseModel(
        key="6",
        value="" + is_selected(current_filter, 6),
        display_name="Minimum phase slow roll-off",
    )
    list.append(r6)
    r7 = ResponseModel(
        key="7",
        value="" + is_selected(current_filter, 7),
        display_name="Minimum phase slow roll-off low dispersion",
    )
    list.append(r7)
    return list


def create_dac_mode_response():
    # 0 I2S Slave mode
    # 1 LJ Slave mode
    # 2 I2S Master mode
    # 3 SPDIF mode
    list = []
    current_dac_mode = dac.get_current_dac_mode()
    r0 = ResponseModel(
        key="0", value=is_selected(current_dac_mode, 0), display_name="I2S Slave Mode"
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1", value=is_selected(current_dac_mode, 1), display_name="LJ Slave mode"
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2", value=is_selected(current_dac_mode, 2), display_name="I2S Master mode"
    )
    list.append(r2)
    r3 = ResponseModel(
        key="3", value=is_selected(current_dac_mode, 3), display_name="SPDIF mode"
    )
    list.append(r3)
    return list


def create_volume_modes_response():
    list = []
    selected = volume_encoder.getButtonKnobMode()
    r0 = ResponseModel(key="0", value=is_selected(selected, 0), display_name="Mute")
    list.append(r0)
    r1 = ResponseModel(
        key="1", value=is_selected(selected, 1), display_name="Disable/enable Volume"
    )
    list.append(r1)
    return list
