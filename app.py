from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

# Делаем базу
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Делаем модель


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.title

# Контекст создания базы


with app.app_context():
    db.create_all()
# Настраиваем сериализацию


Bookfields = {
    'id': fields.Integer,
    'title': fields.String,
    'author': fields.String,
    'date': fields.Integer,
    'publisher': fields.String,
    'isbn': fields.Integer,
}

# Настройки CRUD по REST


class Bookitems(Resource):
    @marshal_with(Bookfields)
    def get(self):
        books = Books.query.all()
        return books

    @marshal_with(Bookfields)
    def post(self):
        data = request.json
        book = Books(title=data['title'], author=data['author'], date=data['date'],
                     publisher=data['publisher'], isbn=data['isbn'])
        db.session.add(book)
        db.session.commit()
        books = Books.query.all()
        return books


class Bookitem(Resource):
    @marshal_with(Bookfields)
    def get(self, id):
        book = Books.query.get_or_404(id)
        return book

    @marshal_with(Bookfields)
    def put(self, id):
        value = request.json
        book = Books.query.get_or_404(id)
        book.title = value['title']
        book.author = value['author']
        book.date = value['date']
        book.publisher = value['publisher']
        book.isbn = value['isbn']
        db.session.commit()
        return book

    @marshal_with(Bookfields)
    def delete(self, id):
        book = Books.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        books = Books.query.all()
        return books


# Настройка маршрутов

api.add_resource(Bookitems, '/')
api.add_resource(Bookitem, '/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
