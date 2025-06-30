from pydantic import BaseModel
from typing import Optional


class RequestModel(BaseModel):
    key: str
    value: str


class ResponseModel(BaseModel):
    key: str
    description: Optional[str]=""
    value: str
    display_name: str
