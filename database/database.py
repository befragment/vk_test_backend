from enum import Enum

import tarantool


class TarantoolTables(str, Enum):
    USERS = 'users'
    USERDATASTORAGE = 'userdatastorage'


def add_user(
    connection: tarantool.Connection,
    user: tuple[int, str, str, str]
):
    connection.insert(space_name=TarantoolTables.USERS, values=user)
    

def add_userdata(
    connection: tarantool.Connection, 
    userdata: tuple[str, dict]
):
    connection.insert(space_name='userdatastorage', values=userdata)
    


conn = tarantool.Connection(host='127.0.0.1',
                            port=3300,
                            user='test',
                            password='test')

tuples = [
    ('123123', {1: 123, 2: 1203123}),
    ('87vw8y', {})
]

for i in tuples:
    response = conn.insert(space_name='userdatastorage', values=i)
    print(response[0])
