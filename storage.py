import json
import os
from model import Event

class StorageException(Exception):
    pass

class LocalStorage:
    def __init__(self, file_path='storage.json'):
        self._file_path = file_path
        self._load_storage()

    def _load_storage(self):
        if not os.path.exists(self._file_path):
            self._storage = {}
            self._save_storage()
        else:
            with open(self._file_path, 'r', encoding='utf-8') as file:
                self._storage = json.load(file)

    def _save_storage(self):
        try:
            with open(self._file_path, 'w', encoding='utf-8') as file:
                json.dump(self._storage, file, ensure_ascii=False, indent=4)
        except Exception as ex:
            raise StorageException(f"Failed to save storage: {ex}")

    def create(self, event: Event) -> str:
        event_dict = event.to_dict()
        if event_dict['id'] in self._storage:
            raise StorageException("Event already exists with this ID")
        self._storage[event_dict['id']] = event_dict
        self._save_storage()
        return event.id

    def list(self):
        return [Event.from_dict(e) for e in self._storage.values()]

    def read(self, event_id: str) -> Event:
        event = self._storage.get(event_id)
        if event:
            return Event.from_dict(event)
        else:
            raise StorageException("Event does not exist")

    def update(self, event_id: str, event: Event):
        if event_id not in self._storage:
            raise StorageException("Event does not exist")
        self._storage[event_id] = event.to_dict()
        self._save_storage()

    def delete(self, event_id: str):
        if event_id not in self._storage:
            raise StorageException("Event does not exist")
        del self._storage[event_id]
        self._save_storage()
