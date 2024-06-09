"""
<EN>
Event Database Management

This module provides a class to interact with the event storage system, allowing for CRUD operations on events.
The storage system is abstracted, and the specific implementation is provided by the `storage` module.

Classes:
    DBException: Custom exception class for database operation errors.
    EventDB: Class for managing events in the storage.

Methods:
    __init__(): Initialize the EventDB with a storage instance.
    create(event: Event) -> str: Create a new event in the storage.
    list() -> List[Event]: List all events from the storage.
    read(event_id: str) -> Event: Read a specific event from the storage.
    update(event_id: str, event: Event): Update an existing event in the storage.
    delete(event_id: str): Delete a specific event from the storage.

Exceptions:
    DBException: Raised for any errors occurring during database operations.
"""
"""
<RUS>
Управление базой данных событий

Этот модуль предоставляет класс для взаимодействия с системой хранения событий, позволяя выполнять операции CRUD с событиями.
Система хранения абстрагирована, а конкретная реализация предоставляется модулем `storage`.

Классы:
    DBException: Пользовательский класс исключений для ошибок операций с базой данных.
    EventDB: Класс для управления событиями в хранилище.

Методы:
    __init__(): Инициализирует EventDB с экземпляром хранилища.
    create(event: Event) -> str: Создать новое событие в хранилище.
    list() -> List[Event]: Получить список всех событий из хранилища.
    read(event_id: str) -> Event: Прочитать конкретное событие из хранилища.
    update(event_id: str, event: Event): Обновить существующее событие в хранилище.
    delete(event_id: str): Удалить конкретное событие из хранилища.

Исключения:
    DBException: Возникает при любых ошибках операций с базой данных.
"""

from typing import List
from model import Event
import storage

class DBException(Exception):
    pass

class EventDB:
    def __init__(self):
        self._storage = storage.LocalStorage()

    def create(self, event: Event) -> str:
        try:
            return self._storage.create(event)
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[Event]:
        try:
            return self._storage.list()
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, event_id: str) -> Event:
        try:
            return self._storage.read(event_id)
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, event_id: str, event: Event):
        try:
            return self._storage.update(event_id, event)
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, event_id: str):
        try:
            return self._storage.delete(event_id)
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
