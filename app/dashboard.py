from flask import Flask, Blueprint, json, render_template, jsonify, session, request, g, redirect, url_for, flash
from app import db
from app.models import Users, Books, Rent
from sqlalchemy.sql import func, distinct

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.route('/<id>', methods=['GET', 'POST'])
def dashboard(id):
    if request.method == 'GET':
        # if g.user is None:
        #     msg ='로그인이 필요한 서비스입니다.'
        #     flash(msg)
        #     return redirect('/home')
        #else:
        rent_list = Books.query.join(Books.rent).filter(Rent.user_id ==  session.get('login')).all()
        
        cur_count = db.session.query(func.count(Rent.user_id)).filter(Rent.status == 1).group_by(Rent.user_id).having(Rent.user_id == session.get('login')).first()[0]
        #cur_count = Rent.query.filter((Rent.user_id == session.get('login')) & (Rent.status == 1)).count()
        total_count = db.session.query(func.count(Rent.user_id)).group_by(Rent.user_id).having(Rent.user_id == session.get('login')).first()[0]
        return render_template('dashboard.html', book_list = rent_list, cur_count = cur_count, total_count = total_count )
    elif request.method == 'POST':
        book_id = request.form.get('book_id')
        book = Books.query.filter(Books.id == book_id).first()
        book.stock += 1
        rent_list = Rent.query.filter((Rent.user_id == session.get('login')) & (Rent.status == 1)).all()

        for rent in rent_list:
            if rent.book_id == book_id:
                rent.status = 0

        db.session.commit()
        return jsonify({'result':'success'})