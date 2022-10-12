from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

# Делаем базу
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Делаем модель


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    data = db.Column(db.Integer(4), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.Integer(13), nullable=False)

    def __repr__(self):
        return self.title

# Настраиваем сериализацию


Bookfields = {
    'id': fields.Integer,
    'title': fields.String(required=True, unique=True, nullable=False),
    'author': fields.String(required=True, nullable=False),
    'date': fields.Positive(required=True, nullable=False),
    'publisher': fields.String,
    'isbn': fields.Integer,
}

# Настройки CRUD по REST


class Bookitems(Resource):
    @marshal_with(Bookfields)
    def get(self):
        books = Book.query.all()
        return books

    @marshal_with(Bookfields)
    def post(self):
        data = request.json
        book = Book(title=data['title'])
        db.session.add(book)
        db.session.commit()
        books = Book.query.all()
        return books


class Bookitem(Resource):
    @marshal_with(Bookfields)
    def get(self, id):
        book = Book.query.filter_by(id=id).first()
        return book

    @marshal_with(Bookfields)
    def put(self, id):
        data = request.json
        book = Book.query.filter_by(id=id).first()
        book.name = data['name']
        db.session.commit()
        return book

    @marshal_with(Bookfields)
    def delete(self, id):
        book = Book.query.filter_by(id=id).first()
        db.session.delete(book)
        db.session.commit()
        books = Book.query.all()
        return books


# Настройка маршрутов

api.add_resource(Bookitems, '/')
api.add_resource(Bookitem, '/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
