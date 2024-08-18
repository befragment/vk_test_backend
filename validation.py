from typing import Any
from pydantic import BaseModel


class LoginModel(BaseModel):
    login: str
    password: str


class TokenResponseModel(BaseModel):
    status: str


class UserWriteModel(BaseModel):
    data: dict[str, Any]


class ServerStatusResponseModel(BaseModel):
    status: str


class UserReadRequestModel(BaseModel):
    keys: list[str]


class ServerDataResponseModel(BaseModel):
    data: dict[str, Any]