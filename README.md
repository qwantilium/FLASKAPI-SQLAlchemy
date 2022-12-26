# FLASKAPI-SQLAlchemy
## Описание проекта:
### Простая API для добавления Книг в список, по принципу CRUD.
Стек: Python 3, Flask, Git, Flask-RESTful, SQLAlchemy.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/qwantilium/FLASKAPI-SQLAlchemy
```

Cоздать и активировать виртуальное окружение(Linux):

```
python -m venv env
```
для linux
```
source env/bin/activate
```
или windows
```
source venv/Scripts/activate
```
далее
```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в рабочую директорию
```
cd FLASKAPI-SQLAlchemy
```

Запустить проект:

```
python app.py
```
API Resource Endpoints
URL Prefix = http://sample_domain/ where sample domain is the root URL of the server HOST.
| EndPoint | Functionality  |
|---|---|---|
| GET / | Get List of Books  |   
|  POST | Post One New Book  |   
| GET  | Get One Certain Book  |   
|  DELETE | Delete One Certain Book  |   
| PUT |  Reenw One Certain Book |   

