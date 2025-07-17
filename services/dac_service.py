import time
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from registry.register import get_instance
from services.utils.dac_util import (
    create_dac_mode_response,
    create_dpll_bandwidth_response,
    create_filter_response,
    create_volume_modes_response,
)

from model.model import RequestModel, ResponseModel
import logging


dac_app = APIRouter(prefix="/dac")
logger = logging.getLogger(__name__)
volume = get_instance("volume")
dac = get_instance("dac")
volume_encoder = get_instance("volumeencoder")
dac_filters = get_instance("dacfilters")


@dac_app.get("/")
async def index():
    response = JSONResponse(content={"message": "abc"})
    return response


@dac_app.get("/oversampling/status")
async def is_oversampling_enabled():
    enabled = dac.is_oversampling_enabled()
    ret = "0"
    if enabled:
        ret = "1"
    response = ResponseModel(key="0", value=ret, display_name=ret)
    return response


@dac_app.put("/oversampling/status")
async def update_oversampling_status(request: RequestModel):
    try:
        dac.enable_disable_oversampling(int(request.value))
        response = ResponseModel(
            key="0", value=request.value, display_name=request.value
        )
        return response
    except Exception as e:
        logger.error(e)


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
        dac.enable_disable_second_order_compensation(int(request.value))
        response = ResponseModel(
            key="0", value=request.value, display_name=request.value
        )
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
        dac.enable_disable_third_order_compensation(int(request.value))
        response = ResponseModel(
            key="0", value=request.value, display_name=request.value
        )
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
    # time.sleep(5)
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


@dac_app.get("/dpll_bandwidth")
async def get_dpll_bandwidth():
    return create_dpll_bandwidth_response()


@dac_app.put("/dpll_bandwidth")
async def update_dpll_bandwidth(request: RequestModel):
    try:
        dac.set_dpll_bandwidth(int(request.value))
        return create_dpll_bandwidth_response()
    except Exception as e:
        logger.error(e)
