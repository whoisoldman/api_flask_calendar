from typing import List, Dict
import json
from model import Event

class LocalStorage:
    def __init__(self):
        self.file_path = 'storage.json'
        try:
            with open(self.file_path, 'r') as file:
                self._storage: Dict[str, Event] = json.load(file)
        except FileNotFoundError:
            self._storage: Dict[str, Event] = {}

    def _save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self._storage, file, default=lambda o: o.__dict__, indent=4)

    def create(self, event: Event) -> str:
        if event.date in self._storage:
            raise Exception('Event already exists for this date')
        self._storage[event.date] = event
        self._save()
        return event.id

    def list(self) -> List[Event]:
        return list(self._storage.values())

    def read(self, event_id: str) -> Event:
        for event in self._storage.values():
            if event.id == event_id:
                return event
        raise Exception('Event not found')

    def update(self, event_id: str, updated_event: Event):
        if updated_event.date in self._storage and self._storage[updated_event.date].id != event_id:
            raise Exception('Event already exists for this date')
        for date, event in self._storage.items():
            if event.id == event_id:
                self._storage[date] = updated_event
                self._save()
                return
        raise Exception('Event not found')

    def delete(self, event_id: str):
        for date in list(self._storage.keys()):
            if self._storage[date].id == event_id:
                del self._storage[date]
                self._save()
                return
        raise Exception('Event not found')
