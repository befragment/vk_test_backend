box.cfg{listen = 3300}

local users = box.schema.space.create('users', { 
    format = {
        { name = 'login', type = 'str', unique = true },
        { name = 'token', type = 'str', unique = true },
        { name = 'data', type = 'map', unique = false }
    },
    if_not_exists = true})

users:create_index('login', { type = 'hash', parts = { 1, 'str' }, if_not_exists = true })
users:create_index('token', { type = 'hash', parts = { 2, 'str' }, if_not_exists = true })