from flask import Flask, jsonify, request

app = Flask(__name__)

#Sample data - In real world scenarios, this could be data from a database
books = [
    {'id': 1, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'image_url': 'https://images.booksense.com/images/798/615/9788194615798.jpg', 'book_name': 'Pride and Prejudice'},
    {'id': 2, 'title': 'Sense and Sensibility', 'author': 'Jane Austen', 'image_url': 'https://m.media-amazon.com/images/I/7161NWQ0jrL._AC_UF1000,1000_QL80_.jpg', 'book_name': 'Sense and Sensibility'},
    {'id': 3, 'title': 'The Tell-Tale Heart', 'author': 'Edgar Allan Poe', 'image_url': 'https://m.media-amazon.com/images/I/81dkKi4oLNL._AC_UF1000,1000_QL80_.jpg', 'book_name': 'The Tell-Tale Heart'},
    {'id': 4, 'title': 'The Raven', 'author': 'Edgar Allan Poe', 'image_url': 'https://embed.cdn.pais.scholastic.com/v1/channels/tso/products/identifiers/isbn/9780439224062/primary/renditions/700', 'book_name': 'The Raven'}
]

# Route for the root URL
@app.route('/')
def index():
    html_content = "<h1>Welcome to the Bookstore API!</h1>"
    html_content += "<h2>Books:</h2>"
    for book in books:
        html_content += f"<p><strong>{book['book_name']}</strong></p>"
        html_content += f"<img src='{book['image_url']}' alt='{book['book_name']}' width='200'><br><br>"
    return html_content

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

# Route to get specific book by ID
@app.route('/books/<int:book_id>', methods =['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify({'book': book[0]})

# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        'id': len(books) + 1,
       'title': request.json['title'],
       'author': request.json['author'],
       'image_url': request.json['image_url'],
       'book_name': request.json['book_name']
    }
    books.append(new_book)
    return jsonify({'message': 'Book created', 'book': new_book}), 201

# Route to update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for books in books if book ['id'] == book_id]
    if len(book) == 0:
        return jsonify({'message': 'Book not found'}), 404
    book[0]['title'] = request.json.get('title', book[0]['title'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['image_url'] = request.json.get('image_url', book[0]['image_url'])
    book[0]['book_name'] = request.json.get('book_name', book[0]['book_name'])
    return jsonify({'message': 'Book updated', 'book': book[0]})

# Route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book ['id'] == book_id]
    if len(book) == 0:
        return jsonify({'message': 'Book not found'}), 404
    books.remove(book[0])
    return jsonify({'message': 'Book deleted', 'book': book[0]})

if __name__ == '__main__':
    app.run(debug=True)