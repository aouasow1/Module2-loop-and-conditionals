from flask import flask, request
from flask_sqlalchemy import SQLAlchemy

 
app = flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(70), unique=True, nullable=False)
    author = db.Column(db.String(90), unique=True, nullable=False)
    publisher = db.Column(db.String(90), unique=True, nullable=False)
    
    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"



@app.route('/')
def index():
    return 'Hello!'

@app.route('/Books')
def get_Books():
    Books = Book.query.all()

    output = []
    for Book in Books:
        Book_data = {'book_name': Book.book_name, 'author': Book.author, 'publisher': Book.publisher}

        output.append(Book_data)


    return {"Books": output}

@app.route('/Books/<id>')
def get_Book(id):
    Book = Book.query.get_or_404(id)
    return {'book_name': Book.book_name, 'author': Book.author, 'publisher': Book.publisher}

@app.route('/Books', methods=['POST'])
def add_Book():
    Book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(Book)
    db.session.commit()
    return {'id': Book.id}




