from pydantic import BaseModel


class RequestModel(BaseModel):
    key: str
    value: str


class ResponseModel(BaseModel):
    key: str
    value: str
    display_name:str
