FROM tarantool/tarantool:latest

COPY myapp.lua /opt/tarantool/myapp.lua

WORKDIR /opt/tarantool

CMD ["tarantool", "/opt/tarantool/myapp.lua"]