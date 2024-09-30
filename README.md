## название приложения
```
flask_project Calendar
```


## запуск приложения в консоле
```
cd C:\Users\user\PycharmProjects\flask_project
C:\Users\user\PycharmProjects\flask_project>main.py
```


## cURL тестирование

### добавление новой заметки
```
POST /api/v1/calendar : создает новое событие
Формат: JSON = {"date": "2024-10-01", "title": "text", "text": "text"}
Формат: "2023-05-29|title|text"
```

### получение всего списка заметок
```
GET /api/v1/calendar
```

### обновление текста заметки по идентификатору / ID == 1 /  новый текст == "new text"
```
PUT /api/v1/calendar/1
```

### удаление заметки по идентификатору / ID == 1
```
DELETE /api/v1/calendar/1
```


## пример исполнения команд с выводом

```
http://localhost:5000/api/v1/calendar
POST {"date": "2024-10-01", "title": "Встреча", "text": "Описание встречи"}

{
        "message": "Событие успешно создано"
    },
    {
        "2024-10-01": {
            "date": "2024-10-01",
            "id": 1,
            "text": "Описание встречи",
            "title": "Встреча"
        }

http://localhost:5000/api/v1/calendar
GET

{
        "message": "Все события"
    },
    {
        "2024-10-01": {
            "date": "2024-10-01",
            "id": 1,
            "text": "Описание встречи",
            "title": "Встреча"
        }

http://localhost:5000/api/v1/calendar/1
PUT {"date": "2024-10-01", "title": "Встреча", "text": "Описание встречи!!!"}

{
        "message": "Событие успешно изменено"
    },
    {
        "2024-10-01": {
            "date": "2024-10-01",
            "id": 1,
            "text": "Описание встречи!!!",
            "title": "Встреча"
        }

http://localhost:5000/api/v1/calendar/1
DELETE

{
    "message": "Событие успешно удалено"
}


```