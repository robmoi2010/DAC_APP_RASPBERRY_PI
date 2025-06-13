from fastapi import APIRouter
from fastapi.responses import JSONResponse
import dac.ess_dac as dac
import factory.system_factory as factory
from factory.system_factory import SYS_OBJECTS
from services.utils.dac_util import (
    create_dac_mode_response,
    create_filter_response,
    create_volume_modes_response,
)
from system import volume_encoder
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


@dac_app.put("/volume/status")
async def disable_enable_volume(request: RequestModel):
    volume.disable_enable_volume(int(request.value))
    disabled = volume.is_volume_disabled()
    return ResponseModel(key="0", value=str(disabled), display_name=str(disabled))


@dac_app.get("/thd_compensation/second_order/status")
async def is_second_order_enabled():
    enabled = dac.is_second_order_compensation_enabled()
    ret = "0"
    if enabled:
        ret = "1"
    response = ResponseModel(key="0", value=ret, display_name=ret)
    return response


@dac_app.put("/thd_compensation/second_order/status")
async def update_second_order_status(request: RequestModel):
    try:
        val = "0"
        if request.value == "0":
            val = "1"
        dac.enable_disable_second_order_compensation(int(val))
        response = ResponseModel(key="0", value=val, display_name=val)
        return response
    except Exception as e:
        logger.error(e)


@dac_app.get("/thd_compensation/third_order/status")
async def is_third_order_enabled():
    enabled = dac.is_third_order_compensation_enabled()
    ret = "0"
    if enabled:
        ret = "1"
    response = ResponseModel(key="0", value=ret, display_name=ret)
    return response


@dac_app.put("/thd_compensation/third_order/status")
async def update_third_order_status(request: RequestModel):
    try:
        val = "0"
        if request.value == "0":
            val = "1"
        dac.enable_disable_third_order_compensation(int(val))
        response = ResponseModel(key="0", value=val, display_name=val)
        return response
    except Exception as e:
        logger.error(e)


@dac_app.get("/volume_modes")
async def get_volume_modes():
    return create_volume_modes_response()


@dac_app.put("/volume_modes")
async def update_volume_mode(request: RequestModel):
    try:
        volume_encoder.setRotaryButtonMode(int(request.value))
        return create_volume_modes_response()
    except Exception as e:
        logger.error(e)


@dac_app.put("/filters")
async def update_filter(request: RequestModel):
    try:
        dac_filters.update_filter(int(request.value))
        return create_filter_response()
    except Exception as e:
        logger.error(e)


@dac_app.get("/filters")
async def get_filters():
    return create_filter_response()


@dac_app.get("/dac_modes")
async def get_dac_modes():
    return create_dac_mode_response()


@dac_app.put("/dac_modes")
async def update_dac_mode(request: RequestModel):
    try:
        dac.set_dac_mode(int(request.value))
        return create_dac_mode_response()
    except Exception as e:
        logger.error(e)
