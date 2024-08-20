from enum import Enum
from sys import stderr
from typing import Any
import logging

import tarantool
import tarantool.error

from config import (
    DB_HOST, DB_PORT, DB_USER, DB_PASS
)


class TarantoolSpaces(str, Enum):
    USERS = 'users'
    


def yield_session():
    try:
        print(DB_HOST, DB_PASS, DB_USER, DB_PORT)
        # не смотрите комментарии ниже
        connection = tarantool.Connection(
            host=DB_HOST, # 127.0.0.1
            port=DB_PORT, # 3302 
            user=DB_USER, # admin 
            password=DB_PASS # presale
        )
        return connection
    except Exception as e:
        logging.info("=========", e)


def add_user(
    user: tuple[str, str, dict]
):
    # print(yield_session())
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