from fastapi import FastAPI

from validation import (
    LoginModel, TokenResponseModel, UserWriteModel,
    ServerStatusResponseModel, UserReadRequestModel, 
    ServerDataResponseModel
)

app = FastAPI()


async def generate_token(log, passw):
    return log[::-1] + passw[::-2]


@app.post('/login', response_model=TokenResponseModel)
async def login(login_data: LoginModel):
    tok = await generate_token(login_data.login, login_data.password)
    return {"token": tok}