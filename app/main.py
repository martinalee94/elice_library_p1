from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for
from app import db
from app.models import Users, Books, Rent
from sqlalchemy.sql import func

bp = Blueprint("main", __name__, url_prefix="/")

@bp.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        keyword = request.args.get('keyword')
        count = db.session.query(db.func.sum(Books.stock)).first()[0]

        if keyword == "":
            return jsonify({'result':'no keyword'})
        elif keyword is not None:
            book_selection = Books.query.filter(Books.book_name.like("%입문%")).all()
            for b in book_selection:
                print(b)
            return render_template('home.html', book_list = book_selection, count = count)
        
        book_list = Books.query.all()
        return render_template('home.html', book_list = book_list, count = count)                       

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
