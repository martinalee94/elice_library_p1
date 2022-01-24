import datetime

from app import db


class Users(db.Model):
    __tablename__ = "users"
    rent = db.relationship("Rent", backref="users")
    rating = db.relationship("Rating", backref="users")

    def __init__(self, user_id, pw_hash, name):
        self.user_id = user_id
        self.pw_hash = pw_hash
        self.name = name

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.String(256), nullable=False, unique=True)
    pw_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False)


class Books(db.Model):
    __tablename__ = "books"
    rent = db.relationship("Rent", backref="books")
    rating = db.relationship("Rating", backref="books")

    def __init__(
        self,
        id,
        book_name,
        publisher,
        author,
        publication_date,
        pages,
        isbn,
        description,
        link,
        image,
        stock,
        rating,
    ):
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
    author = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.String(10), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=False, unique=True)
    stock = db.Column(db.Integer, nullable=False, default=1)
    rating = db.Column(db.Float, nullable=False)


class Rent(db.Model):
    __tablename__ = "rent"

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

    cur = datetime.datetime.now()
    returnDate = cur + datetime.timedelta(days=7)

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    checkout_date = db.Column(db.DateTime, nullable=False, default=cur)
    return_date = db.Column(db.DateTime, nullable=False, default=returnDate)
    status = db.Column(db.Integer, nullable=False, default=1)


class Rating(db.Model):
    __tablename__ = "rating"
    __table_args__ = (
        db.PrimaryKeyConstraint("user_id", "book_id", name="user_rating_uc"),
    )

    def __init__(self, user_id, book_id, point, description):
        self.user_id = user_id
        self.book_id = book_id
        self.point = point
        self.description = description

    cur = datetime.datetime.now()

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    point = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=cur)
    description = db.Column(
        db.String(250), nullable=False
    )  # String이면 250글자까지 된다는 것을 확인했음
