"""
<EN>
Local Storage for Event Management

This module provides a class to handle local storage for events using a JSON file. It includes methods for creating,
listing, reading, updating, and deleting events.

Classes:
    StorageException: Custom exception class for storage operation errors.
    LocalStorage: Class for managing event storage in a local JSON file.

Methods:
    __init__(file_path='storage.json'): Initialize the LocalStorage with the specified file path.
    _load_storage(): Load the storage from the JSON file.
    _save_storage(): Save the current state of storage to the JSON file.
    create(event: Event) -> str: Create a new event and save it to storage.
    list() -> List[Event]: List all events from storage.
    read(event_id: str) -> Event: Read a specific event from storage.
    update(event_id: str, event: Event): Update an existing event in storage.
    delete(event_id: str): Delete a specific event from storage.

Exceptions:
    StorageException: Raised for any errors occurring during storage operations.
"""
"""
<RUS>
Локальное хранилище для управления событиями

Этот модуль предоставляет класс для управления локальным хранилищем событий с использованием JSON-файла. Он включает
методы для создания, перечисления, чтения, обновления и удаления событий.

Классы:
    StorageException: Пользовательский класс исключений для ошибок операций с хранилищем.
    LocalStorage: Класс для управления хранилищем событий в локальном JSON-файле.

Методы:
    __init__(file_path='storage.json'): Инициализирует LocalStorage с указанным путем к файлу.
    _load_storage(): Загружает данные из JSON-файла.
    _save_storage(): Сохраняет текущее состояние хранилища в JSON-файл.
    create(event: Event) -> str: Создает новое событие и сохраняет его в хранилище.
    list() -> List[Event]: Получает список всех событий из хранилища.
    read(event_id: str) -> Event: Читает конкретное событие из хранилища.
    update(event_id: str, event: Event): Обновляет существующее событие в хранилище.
    delete(event_id: str): Удаляет конкретное событие из хранилища.

Исключения:
    StorageException: Возникает при любых ошибках операций с хранилищем.
"""

import json
import os
from model import Event

class StorageException(Exception):
    pass

class LocalStorage:
    def __init__(self, file_path='storage.json'):
        """
        <EN>
        Initialize the LocalStorage with the specified file path.
        Args:
            file_path (str): Path to the JSON file used for storage. Defaults to 'storage.json'.
        """
        """
        <RUS>
        Инициализирует LocalStorage с указанным путем к файлу.
        Аргументы:
            file_path (str): Путь к JSON-файлу, используемому для хранилища. По умолчанию 'storage.json'.
        """
        self._file_path = file_path
        self._load_storage()

    def _load_storage(self):
        """
        <EN>
        Load the storage from the JSON file. If the file does not exist, create an empty storage.
        """
        """
        <RUS>
        Загружает данные из JSON-файла. Если файл не существует, создается пустое хранилище.
        """
        if not os.path.exists(self._file_path):
            self._storage = {}
            self._save_storage()
        else:
            with open(self._file_path, 'r', encoding='utf-8') as file:
                self._storage = json.load(file)

    def _save_storage(self):
        """
        <EN>
        Save the current state of storage to the JSON file.
        Raises:
            StorageException: If there is an error saving the storage.
        """
        """
        <RUS>
        Сохраняет текущее состояние хранилища в JSON-файл.
        Вызывает:
            StorageException: Если возникает ошибка при сохранении хранилища.
        """
        try:
            with open(self._file_path, 'w', encoding='utf-8') as file:
                json.dump(self._storage, file, ensure_ascii=False, indent=4)
        except Exception as ex:
            raise StorageException(f"Failed to save storage: {ex}")

    def create(self, event: Event) -> str:
        """
        <EN>
        Create a new event and save it to storage.
        Args:
            event (Event): The event to be created.
        Returns:
            str: The ID of the created event.
        Raises:
            StorageException: If an event with the same ID already exists.
        """
        """
        <RUS>
        Создает новое событие и сохраняет его в хранилище.
        Аргументы:
            event (Event): Событие, которое нужно создать.
        Возвращает:
            str: ID созданного события.
        Вызывает:
            StorageException: Если событие с таким ID уже существует.
        """
        event_dict = event.to_dict()
        if event_dict['id'] in self._storage:
            raise StorageException("Event already exists with this ID")
        self._storage[event_dict['id']] = event_dict
        self._save_storage()
        return event.id

    def list(self):
        """
        <EN>
        List all events from storage.
        Returns:
            List[Event]: A list of Event instances.
        """
        """
        <RUS>
        Получает список всех событий из хранилища.
        Возвращает:
            List[Event]: Список экземпляров Event.
        """
        return [Event.from_dict(e) for e in self._storage.values()]

    def read(self, event_id: str) -> Event:
        """
        <EN>
        Read a specific event from storage.
        Args:
            event_id (str): The ID of the event to be read.
        Returns:
            Event: The event instance with the specified ID.
        Raises:
            StorageException: If the event does not exist.
        """
        """
        <RUS>
        Читает конкретное событие из хранилища.
        Аргументы:
            event_id (str): ID события, которое нужно прочитать.
        Возвращает:
            Event: Экземпляр события с указанным ID.
        Вызывает:
            StorageException: Если событие не существует.
        """
        event = self._storage.get(event_id)
        if event:
            return Event.from_dict(event)
        else:
            raise StorageException("Event does not exist")

    def update(self, event_id: str, event: Event):
        """
        <EN>
        Update an existing event in storage.
        Args:
            event_id (str): The ID of the event to be updated.
            event (Event): The event instance with updated data.
        Raises:
            StorageException: If the event does not exist.
        """
        """
        <RUS>
        Обновляет существующее событие в хранилище.
        Аргументы:
            event_id (str): ID события, которое нужно обновить.
            event (Event): Экземпляр события с обновленными данными.
        Вызывает:
            StorageException: Если событие не существует.
        """
        if event_id not in self._storage:
            raise StorageException("Event does not exist")
        self._storage[event_id] = event.to_dict()
        self._save_storage()

    def delete(self, event_id: str):
        """
        <EN>
        Delete a specific event from storage.
        Args:
            event_id (str): The ID of the event to be deleted.
        Raises:
            StorageException: If the event does not exist.
        """
        """
        <RUS>
        Удаляет конкретное событие из хранилища.
        Аргументы:
            event_id (str): ID события, которое нужно удалить.
        Вызывает:
            StorageException: Если событие не существует.
        """
        if event_id not in self._storage:
            raise StorageException("Event does not exist")
        del self._storage[event_id]
        self._save_storage()
