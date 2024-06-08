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
