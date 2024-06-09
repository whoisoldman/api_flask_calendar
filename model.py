"""
<EN>
Event Data Model

This module defines a data model for an event using the dataclass decorator. It includes methods for converting
an event instance to a dictionary and creating an event instance from a dictionary.

Classes:
    Event: A dataclass representing an event with attributes for ID, date, title, and text.

Methods:
    to_dict() -> dict: Converts the Event instance to a dictionary.
    from_dict(data: dict) -> Event: Creates an Event instance from a dictionary.
"""
"""
<RUS>
Модель данных события

Этот модуль определяет модель данных для события, используя декоратор dataclass. Он включает методы для преобразования
экземпляра события в словарь и создания экземпляра события из словаря.

Классы:
    Event: Dataclass, представляющий событие с атрибутами для ID, даты, заголовка и текста.

Методы:
    to_dict() -> dict: Преобразует экземпляр Event в словарь.
    from_dict(data: dict) -> Event: Создает экземпляр Event из словаря.
"""

from dataclasses import dataclass

@dataclass
class Event:
    id: str
    date: str
    title: str
    text: str

    def to_dict(self):
        """
        <EN>
        Convert the Event instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Event instance.
        """
        """
        <RUS>
        Преобразует экземпляр Event в словарь.

        Возвращает:
            dict: Словарное представление экземпляра Event.
        """
        return {
            'id': self.id,
            'date': self.date,
            'title': self.title,
            'text': self.text
        }

    @staticmethod
    def from_dict(data):
        """
        <EN>
        Create an Event instance from a dictionary.

        Args:
            data (dict): A dictionary containing the event data.

        Returns:
            Event: An Event instance created from the provided dictionary.
        """
        """
        <RUS>
        Преобразует экземпляр Event в словарь.

        Возвращает:
            dict: Словарное представление экземпляра Event.
        """
        return Event(
            id=data['id'],
            date=data['date'],
            title=data['title'],
            text=data['text']
        )
