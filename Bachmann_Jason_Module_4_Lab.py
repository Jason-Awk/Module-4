from flask import Flask, jsonify, request

app = Flask(__name__)

books = []

class Book:
    def __init__(self, id, book_name, author, publisher):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book_id = len(books) + 1
    new_book = Book(book_id, data['book_name'], data['author'], data['publisher'])
    books.append(new_book)
    return jsonify({
        'message': 'Book has been added.',
        'book': {
            'id': new_book.id,
            'book_name': new_book.book_name,
            'author': new_book.author,
            'publisher': new_book.publisher
        }
    }), 201

@app.route('/books', methods=['GET'])
def get_books():
    all_books = [{
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    } for book in books]
    return jsonify(all_books), 200

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((b for b in books if b.id == id), None)
    if book is None:
        return jsonify({'message': 'Book has not been found.'}), 404
    return jsonify({
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    }), 200

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((b for b in books if b.id == id), None)
    if book is None:
        return jsonify({'message': 'Book has not been found.'}), 404
    
    data = request.get_json()
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)

    return jsonify({
        'message': 'Book has been updated.',
        'book': {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
    }), 200

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book.id != id]
    return jsonify({'message': 'Book has been deleted.'}), 200

if __name__ == '__main__':
    app.run(debug=True)