from enum import Enum
from sys import stderr
from typing import Any

import tarantool
import tarantool.error

from config import (
    DB_HOST, DB_PORT, DB_USER, DB_PASS
)


class TarantoolSpaces(str, Enum):
    USERS = 'users'
    


def yield_session():
    try:
        connection = tarantool.Connection(
            host=DB_HOST, 
            port=DB_PORT, 
            user=DB_USER, 
            password=DB_PASS
        )
        return connection
    except (tarantool.error.NetworkError, ConnectionRefusedError):
        print("Database connection error.", file=stderr)


def add_user(
    user: tuple[str, str, dict]
):
    yield_session().insert(space_name=TarantoolSpaces.USERS, values=user)



def get_users_space():
    return yield_session().select(space_name=TarantoolSpaces.USERS)


def tokens():
    return [user[1] for user in get_users_space()]


def get_db_row_by_token(token: str):
    return yield_session().select(space_name=TarantoolSpaces.USERS, index='token', key=token)


def get_userdata_by_token(token: str):
    return get_db_row_by_token(token)[0][2]


def update_data(token: str, data: dict[Any, Any]):
    row = get_db_row_by_token(token)[0]
    print("row", row)
    print("row[2]", row[2])
    row[2] = data
    yield_session.replace(TarantoolSpaces.USERS, row)