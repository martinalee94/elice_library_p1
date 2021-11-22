from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for
from app import db
from app.models import Users, Books, Rating
import requests

bp = Blueprint("detail", __name__, url_prefix="/books/detail")


@bp.route('/<id>', methods=['GET', 'POST'])
def detail(id):
    if request.method == 'GET':
        book = Books.query.filter(Books.id == id).first()
        #rating_list = Rating.query.filter(Rating.book_id == id).all()
        review_list = db.session.query(Rating, Users).filter(Rating.user_id == Users.id).filter(Rating.book_id == id).order_by(Rating.created_date.desc()).all()
        return render_template('detail.html', book = book, review_list= review_list, book_id = id)
    elif request.method == 'POST':
        if session.get('login') is None:
            return jsonify({'result':'no session'})
        else:
            try:
                review = request.form.get('review')
                rating = request.form.get('rating')
                book_id = request.form.get('book_id')
                user_id = session['login']
                new_review = Rating(user_id, int(book_id), int(rating),review)
                db.session.add(new_review)
                db.session.commit()
                book = Books.query.filter(Books.id == id).first()
                review_list = db.session.query(Rating, Users).filter(Rating.user_id == Users.id).filter(Rating.book_id == id).order_by(Rating.created_date.desc()).all()
                return jsonify({'result':'success'})
            except:
                return jsonify({'result':'duplicated'})
        
