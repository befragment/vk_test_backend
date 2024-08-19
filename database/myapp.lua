box.cfg{listen = 3300}

local users = box.schema.space.create('users', { format = {
    { name = 'id', type = 'unsigned' },
    { name = 'login', type = 'str' },
    { name = 'password', type = 'str' },
    { name = 'token', type = 'str' }
}, if_not_exists = true})

users:create_index('primary', { type = 'hash', parts = { 1, 'unsigned' }, if_not_exists = true })

local userdatastorage = box.schema.space.create('userdatastorage', { format = {
    { name = 'token', type = 'str' },
    { name = 'data', type = 'map' }
}, if_not_exists = true})


userdatastorage:create_index('primary', { type = 'hash', parts = { 1, 'str' }, if_not_exists = true })