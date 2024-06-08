# ps_learning_api_flask_calendar

## Запуск приложения

Для запуска приложения выполните следующую команду:

```
./venv/bin/flask --app ./server.py run
```

После этого сервис календаря будет запущен и доступен по адресу http://127.0.0.1:5000/api/v1/calendar/. Вы можете использовать инструменты, такие как Postman или curl, для тестирования API.

## cURL тестирование

### Добавление нового события

ВНИМАНИЕ: автоматическая (random) инициация <event_id> события. Используется UUID для генерации уникальных идентификаторов:
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -H "Content-Type: application/json" -d '{"data": "2024-06-08|Заголовок события|Текст события"}'
```

### Получение списка всех событий
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### Получение события по идентификатору / <event_id>
```
curl http://127.0.0.1:5000/api/v1/calendar/<event_id>/
```

### Обновление события по идентификатору / <event_id> / Новый заголовок == "Новое название"
```
curl http://127.0.0.1:5000/api/v1/calendar/<event_id>/ -X PUT -H "Content-Type: application/json" -d '{"data": "2024-06-08|Новый загловок события|Новый текст события"}'
```

### Удаление события по идентификатору / ID == <event_id>
```
curl http://127.0.0.1:5000/api/v1/calendar/<event_id>/ -X DELETE
```

## Примеры выполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -H "Content-Type: application/json" -d '{"data": "2024-06-08|Заголовок события|Текст события"}'
```
Ответ: {"message": "Event created"}

```
$ curl http://127.0.0.1:5000/api/v1/calendar/
```
Ответ: [{"id": "<event_id>", "date": "2024-06-08", "title": "Заголовок события", "text": "Текст события"}]

```
$ curl http://127.0.0.1:5000/api/v1/calendar/<event_id>/
```
Ответ: {"id": "<event_id>", "date": "2024-06-08", "title": "Заголовок события", "text": "Текст события"}

```
$ curl http://127.0.0.1:5000/api/v1/calendar/<event_id>/ -X PUT -H "Content-Type: application/json" -d '{"data": "2024-06-08|Новый заголовок события|Новый текст событи"}'
```
Ответ: {"message": "Event updated"}

```
$ curl http://127.0.0.1:5000/api/v1/calendar/<event_id>/
```
Ответ: {"id": "<event_id>", "date": "2024-06-08", "title": "Новый заголовок события", "text": "Новый текст"}

```
$ curl http://127.0.0.1:5000/api/v1/calendar/<event_id>/ -X PUT -H "Content-Type: application/json" -d '{"data": "2024-06-08|Заголовок события слишком длинный|Текст заголовка"}'
```
Ответ: {"error": "Заголовок больше 30 знаков"}

```
$ curl http://127.0.0.1:5000/api/v1/calendar/<event_id>/ -X PUT -H "Content-Type: application/json" -d '{"data": "2024-06-08|Заголовок события|Текст слииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииишком длинный"}'
```
Ответ: {"error": "Текст больше 200 знаков"}

```
$ curl http://127.0.0.1:5000/api/v1/calendar/<event_id>/ -X DELETE
```
Ответ: {"message": "Event deleted"}

```
$ curl http://127.0.0.1:5000/api/v1/calendar/
```
Ответ: []
