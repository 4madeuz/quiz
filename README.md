## Запуск проекта
 
 env.example -> .env

 ./server/quiz/entrypoint.sh CRLF -> LF

# Docker

 docker-compose up -d --build

 docker-compose up

 http://localhost:8080/auth/login - клиент

 http://127.0.0.1:8000/api/openapi#/ - дока


## Добавление теста

- 1 ctr + c test_data.json --> http://127.0.0.1:8000/api/openapi#/
- 2 post to /surveys/ - ctrl + v
- Дальше создать пользователя это post /users/ потом заходишь и в клиентской части уже все 

# Инфа о пользователях

есть два вида пользователей, у которых is_admin == True - админ

у которых is_admin == False - не админ

чтоб не админ смог пройти тест его должен опубликовать(клацнуть зелёный кружечек админ)