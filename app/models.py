from app import db

class Users(db.Model):
    __tablename__ = 'users'
    def __init__(self, user_id, pw_hash, name):
        self.user_id = user_id
        self.pw_hash = pw_hash
        self.name = name

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.String(256), nullable=False, unique=True)
    pw_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False)


class Books(db.Model):
    __tablename__ = 'books'
    def __init__(self, id, book_name, publisher, author, publication_date, pages, isbn, description, link, image, stock, rating):
        self.id = id
        self.book_name = book_name
        self.publisher = publisher
        self.author = author
        self.publication_date = publication_date
        self.pages = pages
        self.isbn = isbn
        self.description = description
        self.link = link
        self.image = image
        self.stock = stock
        self.rating = rating

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_name = db.Column(db.String(256), nullable=False)
    publisher = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(100), nullable=False )
    publication_date =  db.Column(db.String(10), nullable=False)
    pages =  db.Column(db.Integer, nullable=False )
    isbn =  db.Column(db.String(13), unique=True, nullable=False )
    description =  db.Column(db.Text(), nullable=False )
    link =  db.Column(db.String(500), nullable=False )
    image = db.Column(db.String(500), nullable=False, unique=True )
    stock = db.Column(db.Integer, nullable=False, default=1)
    rating = db.Column(db.Float, nullable=False)


class Rent(db.Model):
    __tablename__ = 'rent'
    def __init__(self, user_id, pw_hash, name):
        self.user_id = user_id
        self.pw_hash = pw_hash
        self.name = name

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.String(256), nullable=False, unique=True)
    pw_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False)

class History(db.Model):
    __tablename__ = 'history'
    def __init__(self, user_id, pw_hash, name):
        self.user_id = user_id
        self.pw_hash = pw_hash
        self.name = name

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.String(256), nullable=False, unique=True)
    pw_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False)