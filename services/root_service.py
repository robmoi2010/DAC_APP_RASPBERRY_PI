from contextlib import asynccontextmanager
import traceback
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dac.ess_dac import Dac
from repo.sql_storage import SqlStorage
from services.dac_service import dac_app
from services.system_service import system_app
from services.dsp_service import dsp_app
import registry.register as register
import logging

from services.utils.ws_connection_manager import WSConnectionManager
from tests.volume import test_volume_util

# Logger setup
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# CORS setup
origins = ["http://localhost", "http://localhost:5173", "http://127.0.0.1"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # === Startup ===
    logger.info("App starting up...")
    # start registry queue consumer first
    register.start_consumer()
    await initialize_device()
    await run_tests()

    yield

    # === Shutdown ===


app = FastAPI(lifespan=lifespan)

# Register routers
app.include_router(dac_app)
app.include_router(system_app)
app.include_router(dsp_app)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello World"}


# Cross-cutting middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    try:
        logger.info(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        return response
    except Exception as e:
        logger.error(traceback.format_exc())
        raise


async def initialize_device():
    try:
        connection_manager: WSConnectionManager = await register.get_instance(
            "wsconnectionmanager"
        )
        connection_manager.start_consumers()
    except Exception as e:
        logger.error(traceback.format_exc())
    try:
        dac: Dac = await register.get_instance("dac")
        dac.initialize_dac()
    except Exception as e:
        logger.error(traceback.format_exc())
    try:
        storage: SqlStorage = await register.get_instance("storage")
        storage.initialize()
    except Exception as e:
        logger.error(traceback.format_exc())
    try:
        muses = await register.get_instance("muses72323")
        muses.initialize_volume_chip()
    except Exception as e:
        logger.error(traceback.format_exc())


async def run_tests():
    test_volume_util.TestVolumeUtil().test_map_value()
