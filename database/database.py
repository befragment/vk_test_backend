from enum import Enum
from typing import Any

import tarantool

from config import (
    DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS
)


class TarantoolSpaces(str, Enum):
    USERS = 'users'
    

connection = tarantool.Connection(
    host=DB_HOST, 
    port=DB_PORT, 
    user=DB_USER, 
    password=DB_PASS
)

def add_user(
    user: tuple[str, str, dict]
):
    connection.insert(space_name=TarantoolSpaces.USERS, values=user)



def get_users_space():
    return connection.select(space_name=TarantoolSpaces.USERS)


def tokens():
    return [user[1] for user in get_users_space()]


def get_db_row_by_token(token: str):
    return connection.select(space_name=TarantoolSpaces.USERS, index='token', key=token)


def get_userdata_by_token(token: str):
    return get_db_row_by_token(token)[0][2]


def update_data(token: str, data: dict[Any, Any]):
    row = get_db_row_by_token(token)[0]
    print("row", row)
    print("row[2]", row[2])
    row[2] = data
    connection.replace(TarantoolSpaces.USERS, row)