from model.model import ResponseModel
from services.utils.system_util import is_selected
import dsp.io as dsp


def create_output_response(type):  # 0 mains 1 subwoofer
    # 0 COAX_OUTPUT
    # 1 I2S_OUTPUT0
    # 2 I2S_OUTPUT1
    # 3 I2S_OUTPUT2
    # 4 I2S_OUTPUT3
    current_output = 0
    if type == 1:
        current_output = dsp.get_current_subwoofer_output()
    else:
        current_output = dsp.get_current_main_output()

    list = []
    r0 = ResponseModel(
        key="0", value="" + is_selected(current_output, 0), display_name="COAX_OUTPUT"
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value="" + is_selected(current_output, 1),
        display_name="I2S_OUTPUT0",
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2",
        value="" + is_selected(current_output, 2),
        display_name="I2S_OUTPUT1",
    )
    list.append(r2)
    r3 = ResponseModel(
        key="3",
        value="" + is_selected(current_output, 3),
        display_name="I2S_OUTPUT2",
    )
    list.append(r3)
    r4 = ResponseModel(
        key="4",
        value="" + is_selected(current_output, 4),
        display_name="I2S_OUTPUT3",
    )
    list.append(r4)
    return list


def create_input_response():
    # 0 TOSLINK
    # 1 I2S_INPUT0
    # 2 I2S_INPUT1
    # 3 I2S_INPUT2
    # 4 I2S_INPUT3
    current_input = dsp.get_current_input()
    list = []
    r0 = ResponseModel(
        key="0", value="" + is_selected(current_input, 0), display_name="Toslink"
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value="" + is_selected(current_input, 1),
        display_name="I2S_INPUT0",
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2",
        value="" + is_selected(current_input, 2),
        display_name="I2S_INPUT1",
    )
    list.append(r2)
    r3 = ResponseModel(
        key="3",
        value="" + is_selected(current_input, 3),
        display_name="I2S_INPUT2",
    )
    list.append(r3)
    r4 = ResponseModel(
        key="4",
        value="" + is_selected(current_input, 4),
        display_name="I2S_INPUT3",
    )
    list.append(r4)
    return list
