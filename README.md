# flask_project

# Calendar

# Программа позволяет создавать, изменять, удалять события.

# Запуск проекта в консоле: 
# cd C:\Users\user\PycharmProjects\flask_project
# C:\Users\user\PycharmProjects\flask_project>main.py

# Для тестирования я использую Postman

# Вот список доступных запросов:

# POST /api/v1/calendar: создает новое событие
# GET /api/v1/calendar: возвращает список всех событий
# PUT /api/v1/calendar/<int:event_id>: обновляет информацию о конкретном событии
# DELETE /api/v1/calendar/<int:event_id>: удаляет конкретное событие

# Формат данных для создания и обновления события: "ГГГГ-ММ-ДД|заголовок|текст".

# {"date": "2024-10-01", "title": "Встреча", "text": "Описание встречи"}