from fastapi.responses import JSONResponse
import factory.system_factory as factory
from factory.system_factory import SYS_OBJECTS



dac_app = factory.new(SYS_OBJECTS.FASTAPI)


@dac_app.get("/")
async def index():
    response = JSONResponse(content={"message": "abc"})
    return response



