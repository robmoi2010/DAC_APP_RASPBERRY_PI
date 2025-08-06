import asyncio
import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.model import RequestModel, ResponseModel
from registry.register import get_instance
from services.utils.dac_util import (
    create_dac_mode_response,
    create_dpll_bandwidth_response,
    create_filter_response,
    create_volume_modes_response,
)

# Setup
dac_app = APIRouter(prefix="/dac")
logger = logging.getLogger(__name__)

# Async DI tasks
volume_task = None
dac_task = None
volume_encoder_task = None
dac_filters_task = None


@dac_app.on_event("startup")
async def startup():
    # === Startup ===
    global volume_task
    global dac_task
    global volume_encoder_task
    global dac_filters_task
    volume_task = asyncio.create_task(get_instance("volume"))
    dac_task = asyncio.create_task(get_instance("dac"))
    volume_encoder_task = asyncio.create_task(get_instance("volumeencoder"))
    dac_filters_task = asyncio.create_task(get_instance("dacfilters"))


# Helpers
async def safe_get(task, name):
    obj = await task
    if not obj:
        logger.error(f"[DI] Failed to resolve '{name}'")
    return obj


def bool_response(value: bool) -> ResponseModel:
    val = "1" if value else "0"
    return ResponseModel(key="0", value=val, display_name=val)


# Endpoints


@dac_app.get("/")
async def index():
    return JSONResponse(content={"message": "abc"})


@dac_app.get("/oversampling/status")
async def is_oversampling_enabled():
    dac = await safe_get(dac_task, "dac")
    if not dac:
        return
    return bool_response(dac.is_oversampling_enabled())


@dac_app.put("/oversampling/status")
async def update_oversampling_status(request: RequestModel):
    try:
        dac = await safe_get(dac_task, "dac")
        if not dac:
            return
        dac.enable_disable_oversampling(int(request.value))
        return ResponseModel(key="0", value=request.value, display_name=request.value)
    except Exception as e:
        logger.error(e)


@dac_app.get("/volume/status")
async def is_volume_disabled():
    volume = await safe_get(volume_task, "volume")
    if not volume:
        return
    return ResponseModel(
        key="0",
        value=str(volume.is_volume_disabled()),
        display_name=str(volume.is_volume_disabled()),
    )


@dac_app.put("/volume/status")
async def disable_enable_volume(request: RequestModel):
    volume = await safe_get(volume_task, "volume")
    if not volume:
        return
    volume.disable_enable_volume(int(request.value))
    return ResponseModel(
        key="0",
        value=str(volume.is_volume_disabled()),
        display_name=str(volume.is_volume_disabled()),
    )


@dac_app.get("/thd_compensation/second_order/status")
async def is_second_order_enabled():
    dac = await safe_get(dac_task, "dac")
    if not dac:
        return
    return bool_response(dac.is_second_order_compensation_enabled())


@dac_app.put("/thd_compensation/second_order/status")
async def update_second_order_status(request: RequestModel):
    try:
        dac = await safe_get(dac_task, "dac")
        if not dac:
            return
        dac.enable_disable_second_order_compensation(int(request.value))
        return ResponseModel(key="0", value=request.value, display_name=request.value)
    except Exception as e:
        logger.error(e)


@dac_app.get("/thd_compensation/third_order/status")
async def is_third_order_enabled():
    dac = await safe_get(dac_task, "dac")
    if not dac:
        return
    return bool_response(dac.is_third_order_compensation_enabled())


@dac_app.put("/thd_compensation/third_order/status")
async def update_third_order_status(request: RequestModel):
    try:
        dac = await safe_get(dac_task, "dac")
        if not dac:
            return
        dac.enable_disable_third_order_compensation(int(request.value))
        return ResponseModel(key="0", value=request.value, display_name=request.value)
    except Exception as e:
        logger.error(e)


@dac_app.get("/volume_modes")
async def get_volume_modes():
    return create_volume_modes_response(
        await safe_get(volume_encoder_task, "volumeencoder")
    )


@dac_app.put("/volume_modes")
async def update_volume_mode(request: RequestModel):
    try:
        volume_encoder = await safe_get(volume_encoder_task, "volumeencoder")
        if not volume_encoder:
            return
        volume_encoder.setRotaryButtonMode(int(request.value))
        return create_volume_modes_response(volume_encoder)
    except Exception as e:
        logger.error(e)


@dac_app.get("/filters")
async def get_filters():
    return create_filter_response(await safe_get(dac_filters_task, "dacfilters"))


@dac_app.put("/filters")
async def update_filter(request: RequestModel):
    try:
        dac_filters = await safe_get(dac_filters_task, "dacfilters")
        if not dac_filters:
            return
        dac_filters.update_filter(int(request.value))
        return create_filter_response(dac_filters)
    except Exception as e:
        logger.error(e)


@dac_app.get("/dac_modes")
async def get_dac_modes():
    return create_dac_mode_response(await safe_get(dac_task, "dac"))


@dac_app.put("/dac_modes")
async def update_dac_mode(request: RequestModel):
    try:
        dac = await safe_get(dac_task, "dac")
        if not dac:
            return
        dac.set_dac_mode(int(request.value))
        return create_dac_mode_response(dac)
    except Exception as e:
        logger.error(e)


@dac_app.get("/dpll_bandwidth")
async def get_dpll_bandwidth():
    return create_dpll_bandwidth_response(await safe_get(dac_task, "dac"))


@dac_app.put("/dpll_bandwidth")
async def update_dpll_bandwidth(request: RequestModel):
    try:
        dac = await safe_get(dac_task, "dac")
        if not dac:
            return
        dac.set_dpll_bandwidth(int(request.value))
        return create_dpll_bandwidth_response(dac)
    except Exception as e:
        logger.error(e)
