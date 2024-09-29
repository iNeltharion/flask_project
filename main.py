from flask import Flask, request, jsonify

app = Flask(__name__)

events = {}

@app.route('/api/v1/calendar', methods=['GET'])
def get_events():
    if events:
        return jsonify({'message': 'Все события'}, events)
    else:
        return jsonify({'message': 'Событий нет'})

@app.route('/api/v1/calendar', methods=['POST'])
def create_event():
    data = request.json
    title, text, date = data['title'], data['text'], data['date']

    if len(title) > 30 or len(text) > 200:
        return jsonify({'error': 'Превышена длина заголовка или текста'})
    if any(e['date'] == date for e in events.values()):
        return jsonify({'error': 'Событие на эту дату уже существует'})

    new_event = {'id': len(events) + 1, 'date': date, 'title': title, 'text': text}
    events[date] = new_event
    return jsonify({'message': 'Событие успешно создано'}, events)


@app.route('/api/v1/calendar/<int:event_id>/', methods=['PUT'])
def update_event(event_id):
    data = request.json
    title, text = data['title'], data['text']

    for event in events.values():
        if event['id'] == event_id:
            event['title'], event['text'] = title, text
            return jsonify({'message': 'Событие успешно изменено'}, events)
    return jsonify({'error': 'Событие не найдено'})

@app.route('/api/v1/calendar/<int:event_id>/', methods=['DELETE'])
def delete_event(event_id):
    for date, event in events.items():
        if event['id'] == event_id:
            del events[date]
            return jsonify({'message': 'Событие успешно удалено'})
    return jsonify({'error': 'Событие не найдено'})


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug=True)