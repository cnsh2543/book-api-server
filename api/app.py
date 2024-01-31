from flask import Flask, jsonify, request
import copy

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    }
]

                

@app.route("/")
def index():
    args = ["id", "publication_year", "genre", "title", "author"]
    param_pairs = []
    # create tuple pairs
    for arg in args:
        param_pairs.append((arg, request.args.get(arg)))

    # deep copy dictinoary
    matching_books = copy.deepcopy(books)

    for param_pair in param_pairs:
        if param_pair[1] is not None and param_pair[1] != '':
            matching_books = [book for book in matching_books if param_pair[1].lower() in str(book.get((param_pair[0]))).lower()]
            
    return jsonify(matching_books)

