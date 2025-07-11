from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from services.dac_service import dac_app
from services.system_service import system_app
from services.dsp_service import dsp_app

import logging

origins = ["http://localhost", "http://localhost:5173", "http//127.0.0.1"]
app = FastAPI()
app.include_router(dac_app)
app.include_router(system_app)
app.include_router(dsp_app)

logger = logging.getLogger(__name__)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
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
    try:
        # log client ips and destination endpoint
        pass
    except Exception as e:
        pass
    return response
