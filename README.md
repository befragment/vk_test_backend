# В этом репозитории представлено API для KV хранилища на базе tarantool


## Для документации я воспользовался встроенной утилитой фреймворка FastApi под названием SwaggerUI

### 1. Запуск приложения через docker
```bash
cd database 
docker build -t my-tarantool-image .
docker run -d --name my-tarantool-container my-tarantool-image

cd ..
docker build . -t app:latest
docker run -d -p 1234:8000 app 

docker compose build 
docker compose up
```
### 2. Эндпоинты
Начальная страница с документацией
![Image alt](https://github.com/befragment/vk_test_backend/raw/master/docs/swagger_intro.png)

Отправили запрос на endpoint login, справа во вкладке Network/Response мы получили токен авторизации

![Image alt](https://github.com/befragment/vk_test_backend/raw/master/docs/getting_token.png)

Нажимаем на "Authorize" и во всплывающем окне вводим наш токен, чтобы получить доступ к защищенным эндпоинтам

![Image alt](https://github.com/befragment/vk_test_backend/raw/master/docs/authorization.png)

Передали словарь на эндпоинт write, кроме того, мы передали заголовок Authentication c полученным ранее токеном 

![Image alt](https://github.com/befragment/vk_test_backend/raw/master/docs/write_endpoint.png)

Выбрали из бд значения соответсвующие запрашиваемым ключам

![Image alt](https://github.com/befragment/vk_test_backend/raw/master/docs/read_endpoint.png)

