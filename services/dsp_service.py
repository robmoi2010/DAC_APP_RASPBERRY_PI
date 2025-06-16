import logging

from fastapi import APIRouter
from registry.register import get_instance
from model.model import RequestModel
from services.utils.dsp_util import create_input_response, create_output_response

dsp_app = APIRouter(prefix="/dsp")
logger = logging.getLogger(__name__)

dsp = get_instance("dspio")


@dsp_app.put("/output/subwoofer")
async def update_subwoofer_output(request: RequestModel):
    try:
        dsp.update_subwoofer_output(request.value)
        return create_output_response(1)
    except Exception as e:
        logger.error(e)


@dsp_app.get("/output/subwoofer")
async def get_subwoofer_outputs():
    return create_output_response(1)


@dsp_app.put("/output/mains")
async def update_mains_output(request: RequestModel):
    try:
        dsp.update_main_output(request.value)
        return create_output_response(0)
    except Exception as e:
        logger.error(e)


@dsp_app.get("/output/mains")
async def get_mains_outputs():
    return create_output_response(0)


@dsp_app.put("/input")
async def update_input(request: RequestModel):
    try:
        dsp.update_current_input(request.value)
        return create_input_response()
    except Exception as e:
        logger.error(e)


@dsp_app.get("/input")
async def get_inputs():
    return create_input_response()
