from fastapi import Depends, FastAPI, HTTPException
from starlette import status
import tarantool
import uvicorn

from database.database import add_user, get_userdata_by_token, update_data
from database.validation import (
    LoginModel, ServerDataResponseModel, 
    UserReadRequestModel, TokenResponseModel,
    ServerStatusResponseModel, UserWriteModel
)
from auth.auth import create_access_token, get_token

app = FastAPI(title="vk tarantool api")

@app.post(
    '/login', 
    response_model=TokenResponseModel
)
async def login(user: LoginModel):
    try:
        token = create_access_token(user.login + user.password)
        add_user((user.login, token, {}))
    # if we do nothing with this exception it gives 500 error, which is not really true
    except tarantool.error.DatabaseError: 
        raise HTTPException(status.HTTP_409_CONFLICT, detail="User already exists")

    return {"token": token}


@app.post(
    "/write",
    response_model=ServerStatusResponseModel,
)
async def write(new_data: UserWriteModel, token: str = Depends(get_token)):
    new_data_dict = get_userdata_by_token(token) |  new_data.model_dump()
    update_data(token, new_data_dict)
    return {"status": "success"}


@app.post(
    "/read",
    response_model=ServerDataResponseModel,
)
def read(data_to_show: UserReadRequestModel, token: str = Depends(get_token)):
    user_data = get_userdata_by_token(token)

    if not data_to_show:
        return user_data
    
    if 'data' in user_data:
        user_data |= user_data['data']

    output_data = {}
    for key in data_to_show.keys:
        if key in user_data:
            output_data[key] = user_data[key]

    return {"data": output_data}


if __name__ == "__main__":
    uvicorn.run(
        app='main:app', 
        host="127.0.0.1", 
        port=8001, 
        reload=False, 
        access_log=False
    )