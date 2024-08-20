box.cfg{listen = 3302}

local users = box.schema.space.create('users', {
    format = {
        { name = 'login', type = 'str', unique = true },
        { name = 'token', type = 'str', unique = true },
        { name = 'data', type = 'map', unique = false }
    },
    if_not_exists = true})

users:create_index('login', { type = 'hash', parts = { 1, 'str' }, if_not_exists = true })
users:create_index('token', { type = 'hash', parts = { 2, 'str' }, if_not_exists = true })

box.schema.user.passwd('admin', 'presale')
print("============== admin created")
box.schema.user.grant('admin', 'read,write', 'space', 'users')
print("============== admin priveleges granted")