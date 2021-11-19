from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for
from app import db
from app.models import Users, Books
from sqlalchemy.sql import func

bp = Blueprint("books", __name__, url_prefix="/")

@bp.route('/home', methods=['GET'])
def home():
    if request.method == 'GET':
        keyword = request.form.get('keyword')
        count = db.session.query(db.func.sum(Books.stock)).first()[0]
        if keyword is None:
            book_list = Books.query.all()
            return render_template('home.html', book_list = book_list, count = count)
        else:
            book_selection = Books.query.filter(Books.book_name.like(f"%{keyword}%")).all()
            return render_template('home.html', book_list = book_selection, count = count)
        # else: