from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from services.dac_service import dac_app
from services.system_service import system_app
import factory.system_factory as factory
from factory.system_factory import SYS_OBJECTS
import logging

origins = ["http://localhost", "http://localhost:5173", "http//127.0.0.1"]
app = factory.new(SYS_OBJECTS.FASTAPI)
app.include_router(dac_app.router, prefix="/dac")
app.include_router(system_app)

logger = logging.getLogger(__name__)



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # "*" allows all origins
    # allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def read_root():
    return "message: Hello World"


@app.middleware("http")
async def middleware(
    request: Request, call_next
):  # for future cross-cutting functionality
    response = await call_next(request)
    return response
