from typing import Any
from pydantic import BaseModel

class LoginModel(BaseModel):
    login: str
    password: str


class TokenResponseModel(BaseModel):
    token: str 


class UserWriteModel(BaseModel):
    data: dict[Any, Any]


class ServerStatusResponseModel(BaseModel):
    status: str = "success"


class UserReadRequestModel(BaseModel):
    keys: list[Any]


class ServerDataResponseModel(BaseModel):
    data: dict[Any, Any]