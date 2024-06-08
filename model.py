from dataclasses import dataclass

@dataclass
class Event:
    id: str
    date: str  # формат 'ГГГГ-ММ-ДД'
    title: str
    text: str
