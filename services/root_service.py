from fastapi import Request
from services.dac_service import dac_app
from services.system_service import system_app
import factory.system_factory as factory
from factory.system_factory import SYS_OBJECTS

app = factory.new(SYS_OBJECTS.FASTAPI)
app.mount("/dac", dac_app)
app.mount("/system", system_app)


@app.middleware("http")
async def middleware(
    request: Request, call_next
):  # for future cross-cutting functionality
    response = await call_next(request)
    return response
