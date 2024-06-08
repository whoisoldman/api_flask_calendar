from dataclasses import dataclass

@dataclass
class Event:
    id: str
    date: str
    title: str
    text: str

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'title': self.title,
            'text': self.text
        }

    @staticmethod
    def from_dict(data):
        return Event(
            id=data['id'],
            date=data['date'],
            title=data['title'],
            text=data['text']
        )
