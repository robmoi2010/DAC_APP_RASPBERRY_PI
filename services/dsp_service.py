import asyncio
import logging
import traceback
from fastapi import APIRouter
from registry.register import get_instance
from model.model import RequestModel
from services.utils.dsp_util import create_input_response, create_output_response

# Setup
dsp_app = APIRouter(prefix="/dsp")
logger = logging.getLogger(__name__)

# Async DI task
dsp_task = None


@dsp_app.on_event("startup")
async def startup():
    # === Startup ===
    global dsp_task
    dsp_task = asyncio.create_task(get_instance("dspio"))


# Helper
async def safe_get(task, name):
    obj = await task
    if not obj:
        logger.error(f"[DI] Failed to resolve '{name}'")
    return obj


# Subwoofer output
@dsp_app.put("/output/subwoofer")
async def update_subwoofer_output(request: RequestModel):
    try:
        dsp = await safe_get(dsp_task, "dspio")
        if not dsp:
            return
        dsp.update_subwoofer_output(request.value)
        return create_output_response(1, dsp)
    except Exception as e:
        logger.error(traceback.format_exc())


@dsp_app.get("/output/subwoofer")
async def get_subwoofer_outputs():
    return create_output_response(1, await safe_get(dsp_task, "dsp"))


# Mains output
@dsp_app.put("/output/mains")
async def update_mains_output(request: RequestModel):
    try:
        dsp = await safe_get(dsp_task, "dspio")
        if not dsp:
            return
        dsp.update_main_output(request.value)
        return create_output_response(0, dsp)
    except Exception as e:
        logger.error(traceback.format_exc())


@dsp_app.get("/output/mains")
async def get_mains_outputs():
    return create_output_response(0, await safe_get(dsp_task, "dsp"))


# Input selector
@dsp_app.put("/input")
async def update_input(request: RequestModel):
    try:
        dsp = await safe_get(dsp_task, "dspio")
        if not dsp:
            return
        dsp.update_current_input(request.value)
        return create_input_response(dsp)
    except Exception as e:
        logger.error(traceback.format_exc())


@dsp_app.get("/input")
async def get_inputs():
    return create_input_response(await safe_get(dsp_task, "dsp"))
