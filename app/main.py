from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for, abort
from app import db
from app.models import Users, Books, Rent, Rating
from sqlalchemy.sql import func
import math

bp = Blueprint("main", __name__, url_prefix="/home")

@bp.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        page = request.args.get('pageNumber')
        page = 0 if not page else 8 * (int(page) - 1)
        cur_count = db.session.query(db.func.sum(Books.stock)).first()[0]
        book_list = Books.query.all()
        book_count = len(book_list)
        total_page = math.ceil(book_count / 8)

        if page > total_page:
            abort(404)
            
        sum_list = db.session.query(Rating.book_id, func.sum(Rating.point)).group_by(Rating.book_id).all()
        count_list = db.session.query(Rating.book_id, func.count(Rating.book_id)).group_by(Rating.book_id).all()

        for s, c in zip(sum_list, count_list):
            book = Books.query.filter(Books.id == int(s[0])).first()
            book.rating = round(int(s[1]) / int(c[1]))
            db.session.commit()

        book_list = book_list[page:page+8]
        #return jsonify(book_list = book_list, cur_count = cur_count, book_count = book_count, total_page = total_page)
        return render_template('home.html', book_list = book_list, cur_count = cur_count, book_count = book_count, total_page = total_page)                       

    elif request.method == 'POST':
        if session.get('login') is not None:
            book_id = int(request.form.get('book_id'))
            book = Books.query.filter(Books.id == book_id).first()
            if book.stock == 0:
                return jsonify({'result':'no stock'})
                
            user = Users.query.filter(Users.id == session['login']).first()
            book.stock -= 1
            rentInfo = Rent.query.filter((Rent.user_id == user.id) & (Rent.status == 1)).all()
            
            if rentInfo is not None:
                for rent in rentInfo:
                    if rent.book_id == book.id:
                        return jsonify({'result':'rent exists'})

            rentBook = Rent(user.id, book_id)
            db.session.add(rentBook)
            db.session.commit()
            return jsonify({'result':'success'})
        else:
            return jsonify({'result':'no session'})


@bp.route('/search/', methods=['GET'])
def search():
    if request.method == 'GET':
        keyword = request.args.get('keyword')
        '''
        if keyword == "":
            return jsonify({'result':'no keyword'})
        elif keyword is not None:
            book_selection = Books.query.filter(Books.book_name.like(f"%{keyword}%")).all()
            count = len(book_selection)

            cur_count = db.session.query(db.func.sum(Books.stock)).first()[0]
            book_list = Books.query.all()
            book_count = len(book_list)
            total_page = math.ceil(book_count / 8)
            sum_list = db.session.query(Rating.book_id, func.sum(Rating.point)).group_by(Rating.book_id).all()
            count_list = db.session.query(Rating.book_id, func.count(Rating.book_id)).group_by(Rating.book_id).all()

            for s, c in zip(sum_list, count_list):
                book = Books.query.filter(Books.id == int(s[0])).first()
                book.rating = round(int(s[1]) / int(c[1]))
                db.session.commit()

            book_list = book_list[page:page+8]            
            return render_template('home.html', book_list = book_selection, cur_count = cur_count, book_count = book_count, total_page = total_page)
            '''