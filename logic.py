"""
<EN>
Event Logic Management

This module provides a class to handle the business logic for managing events, including validation and interaction
with the underlying database through the EventDB class.

Classes:
    LogicException: Custom exception class for logic operation errors.
    EventLogic: Class for managing the business logic of events.

Constants:
    TITLE_LIMIT (int): Maximum allowed length for the event title.
    TEXT_LIMIT (int): Maximum allowed length for the event text.

Methods:
    __init__(): Initialize the EventLogic with a database instance.
    _validate_event(event: model.Event): Validate the event object to ensure it meets business rules.
    create(event: model.Event) -> str: Create a new event after validation.
    list() -> List[model.Event]: List all events.
    read(event_id: str) -> model.Event: Read a specific event by ID.
    update(event_id: str, event: model.Event): Update an existing event after validation.
    delete(event_id: str): Delete a specific event by ID.

Exceptions:
    LogicException: Raised for any errors occurring during logic operations.
"""
"""
<RUS>
Управление логикой событий

Этот модуль предоставляет класс для обработки бизнес-логики управления событиями, включая валидацию и взаимодействие
с базой данных через класс EventDB.

Классы:
    LogicException: Пользовательский класс исключений для ошибок логических операций.
    EventLogic: Класс для управления бизнес-логикой событий.

Константы:
    TITLE_LIMIT (int): Максимально допустимая длина заголовка события.
    TEXT_LIMIT (int): Максимально допустимая длина текста события.

Методы:
    __init__(): Инициализирует EventLogic с экземпляром базы данных.
    _validate_event(event: model.Event): Проверяет объект события на соответствие бизнес-правилам.
    create(event: model.Event) -> str: Создает новое событие после проверки.
    list() -> List[model.Event]: Получает список всех событий.
    read(event_id: str) -> model.Event: Считывает конкретное событие по ID.
    update(event_id: str, event: model.Event): Обновляет существующее событие после проверки.
    delete(event_id: str): Удаляет конкретное событие по ID.

Исключения:
    LogicException: Возникает при любых ошибках логических операций.
"""

from typing import List
import model
import db

TITLE_LIMIT = 30
TEXT_LIMIT = 200

class LogicException(Exception):
    pass

class EventLogic:
    def __init__(self):
        self._event_db = db.EventDB()

    @staticmethod
    def _validate_event(event: model.Event):
        if event is None:
            raise LogicException("Event is None")
        if event.title is None or len(event.title) > TITLE_LIMIT:
            raise LogicException(f"Title length exceeds maximum limit of {TITLE_LIMIT} characters")
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"Text length exceeds maximum limit of {TEXT_LIMIT} characters")

    def create(self, event: model.Event) -> str:
        self._validate_event(event)
        try:
            return self._event_db.create(event)
        except Exception as ex:
            raise LogicException(f"Failed to create event: {ex}")

    def list(self) -> List[model.Event]:
        try:
            return self._event_db.list()
        except Exception as ex:
            raise LogicException(f"Failed to list events: {ex}")

    def read(self, event_id: str) -> model.Event:
        try:
            event = self._event_db.read(event_id)
            if event is None:
                raise LogicException(f"Event with ID {event_id} not found")
            return event
        except Exception as ex:
            raise LogicException(f"Failed to read event: {ex}")

    def update(self, event_id: str, event: model.Event):
        self._validate_event(event)
        try:
            if self._event_db.read(event_id) is None:
                raise LogicException(f"Event with ID {event_id} not found")
            return self._event_db.update(event_id, event)
        except Exception as ex:
            raise LogicException(f"Failed to update event: {ex}")

    def delete(self, event_id: str):
        try:
            if self._event_db.read(event_id) is None:
                raise LogicException(f"Event with ID {event_id} not found")
            return self._event_db.delete(event_id)
        except Exception as ex:
            raise LogicException(f"Failed to delete event: {ex}")
