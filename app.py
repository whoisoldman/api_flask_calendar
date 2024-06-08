from flask import Flask, request, jsonify
from logic import EventLogic, LogicException
from model import Event
import uuid

app = Flask(__name__)
logic = EventLogic()

@app.route('/api/v1/calendar/', methods=['POST'])
def create_event():
    data = request.get_json(force=True, silent=True)  # Используем force=True, чтобы принудительно разбирать JSON, и silent=True, чтобы избежать вывода ошибок при некорректном JSON
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    try:
        date, title, text = data['data'].split('|')
        if len(title) > 30 or len(text) > 200:
            return jsonify({'error': 'Validation error'}), 400
        event = Event(id=str(uuid.uuid4()), date=date, title=title, text=text)
        logic.create(event)
        return jsonify({'message': 'Event created'}), 201
    except LogicException as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/v1/calendar/', methods=['GET'])
def list_events():
    try:
        events = logic.list()
        return jsonify([event.__dict__ for event in events]), 200
    except LogicException as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/v1/calendar/<event_id>/', methods=['GET'])
def read_event(event_id):
    try:
        event = logic.read(event_id)
        return jsonify(event.__dict__), 200
    except LogicException as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/v1/calendar/<event_id>/', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    try:
        date, title, text = data.split('|')
        if len(title) > 30 or len(text) > 200:
            return jsonify({'error': 'Validation error'}), 400
        event = Event(id=event_id, date=date, title=title, text=text)
        logic.update(event_id, event)
        return jsonify({'message': 'Event updated'}), 200
    except LogicException as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/v1/calendar/<event_id>/', methods=['DELETE'])
def delete_event(event_id):
    try:
        logic.delete(event_id)
        return jsonify({'message': 'Event deleted'}), 200
    except LogicException as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
