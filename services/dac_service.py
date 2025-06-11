from fastapi import APIRouter
from fastapi.responses import JSONResponse
from dac.ess_dac import get_current_dac_mode
import factory.system_factory as factory
from factory.system_factory import SYS_OBJECTS
from general import volume_encoder
from model.model import RequestModel, ResponseModel
import logging

import dac.dac_filters as dac_filters

dac_app = APIRouter(prefix="/dac")
logger = logging.getLogger(__name__)
volume = factory.new(SYS_OBJECTS.DAC_VOLUME)


@dac_app.get("/")
async def index():
    response = JSONResponse(content={"message": "abc"})
    return response


@dac_app.get("/volume/status")
async def is_volume_disabled():
    disabled = volume.is_volume_disabled()
    response = ResponseModel(key="0", value=str(disabled), display_name=str(disabled))
    return response


@dac_app.get("/volume_modes")
async def get_volume_modes():
    selected = volume_encoder.getButtonKnobMode()
    response = ResponseModel(key="0", value=str(""), display_name=str(""))
    return response


@dac_app.put("/volume/status")
async def disable_enable_volume(request: RequestModel):
    
    return request


@dac_app.put("/filters")
async def update_filter(request: RequestModel):
    try:
        dac_filters.update_filter(int(request.value))
        return request
    except Exception as e:
        logger.error(e)


@dac_app.get("/filters")
async def get_filters():
    # 0 Minimum phase
    # 1 Linear phase apodizing first roll-off
    # 2 Linear phase fast roll-off
    # 3 Linear phase slow roll-off low ripple
    # 4 Linear phase slow roll-off
    # 5 Minimum phase fast roll-off
    # 6 Minimum phase slow roll-off
    # 7 Minimum phase slow roll-off low dispersion
    current_filter = dac_filters.get_current_filter()
    print(str(current_filter != 11))
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


@dac_app.get("/dac_modes")
async def get_dac_modes():
    # 0 I2S Slave mode
    # 1 LJ Slave mode
    # 2 I2S Master mode
    # 3 SPDIF mode
    list = []
    current_dac_mode = get_current_dac_mode()
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


@dac_app.put("/dac_modes")
async def update_dac_mode(request: RequestModel):
    return request


def is_selected(current_item, index):
    selected = "0"
    if current_item == index:
        selected = "1"
    return selected
