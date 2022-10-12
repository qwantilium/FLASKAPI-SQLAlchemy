from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with


app = Flask(__name__)
api = Api(app)




fields = {
    'title': fields.String(required=True, unique=True, nullable=False),
    'author': fields.String(required=True,nullable=False),
    'date': fields.Positive(required=True, nullable=False),
    'publisher': fields.String,

}

class Books(Resource):
    def get(self):
        return {'hello': 'world'}

    def

class Book(Resource):
    def get(self):
        return

    def post(self):
        return



api.add_resource(Books, '/')
api.add_resource(Book, '/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
