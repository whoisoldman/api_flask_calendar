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
