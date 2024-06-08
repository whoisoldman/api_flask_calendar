# ps_learning_api_flask_calendar

## Запуск приложения

Для запуска приложения выполните следующую команду:

```
./venv/bin/flask --app ./server.py run
```

После этого сервис календаря будет запущен и доступен по адресу http://127.0.0.1:5000/api/v1/calendar/. Вы можете использовать инструменты, такие как Postman или curl, для тестирования API.

## cURL тестирование

### Добавление нового события
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -H "Content-Type: application/json" -d '{"data": "2024-06-08|Название события|Текст события"}'
```

### Получение списка всех событий
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### Получение события по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```

### Обновление события по идентификатору / ID == 1 / Новый заголовок == "Новое название"
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -H "Content-Type: application/json" -d '{"data": "2024-06-08|Новое название|Новый текст"}'
```

### Удаление события по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```

## Примеры выполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -H "Content-Type: application/json" -d '{"data": "2024-06-08|Название события|Текст события"}'
{"message": "Event created"}

$ curl http://127.0.0.1:5000/api/v1/calendar/
[{"id": "1", "date": "2024-06-08", "title": "Название события", "text": "Текст события"}]

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
{"id": "1", "date": "2024-06-08", "title": "Название события", "text": "Текст события"}

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -H "Content-Type: application/json" -d '{"data": "2024-06-08|Новое название|Новый текст"}'
{"message": "Event updated"}

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
{"id": "1", "date": "2024-06-08", "title": "Новое название", "text": "Новый текст"}

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -H "Content-Type: application/json" -d '{"data": "2024-06-08|Новое название слишком длинное|Новый текст"}'
{"error": "Validation error"}

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -H "Content-Type: application/json" -d '{"data": "2024-06-08|Новый заголовок|Новый текст слишком длинный"}'
{"error": "Validation error"}

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
{"message": "Event deleted"}

$ curl http://127.0.0.1:5000/api/v1/calendar/
[]
```
