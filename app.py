from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

books = [
    {
        "id": 1,
        "book_name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Charles Scribner's Sons"
    },
    {
        "id": 2,
        "book_name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J. B. Lippincott & Co."
    }
]

class Book(Resource):
    def get(self, id):
        for book in books:
            if book["id"] == id:
                return book, 200
        return "Book not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("book_name")
        parser.add_argument("author")
        parser.add_argument("publisher")
        args = parser.parse_args()

        for book in books:
            if book["id"] == id:
                return "Book with id {} already exists".format(id), 400

        book = {
            "id": id,
            "book_name": args["book_name"],
            "author": args["author"],
            "publisher": args["publisher"]
        }
        books.append(book)
        return book, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("book_name")
        parser.add_argument("author")
        parser.add_argument("publisher")
        args = parser.parse_args()

        for book in books:
            if book["id"] == id:
                book["book_name"] = args["book_name"]
                book["author"] = args["author"]
                book["publisher"] = args["publisher"]
                return book, 200
        
        book = {
            "id": id,
            "book_name": args["book_name"],
            "author": args["author"],
            "publisher": args["publisher"]
        }
        books.append(book)
        return book, 201

    def delete(self, id):
        global books
        books = [book for book in books if book["id"] != id]
        return "Book is deleted", 204

api.add_resource(Book, "/book/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
