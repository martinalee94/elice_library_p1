from flask import Flask, Blueprint, json, render_template, jsonify, session, request, g, redirect, url_for, flash
from app import db
from app.models import Users, Books, Rent
from sqlalchemy.sql import func, distinct
import datetime

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.route('/<id>', methods=['GET', 'POST'])
def dashboard(id):
    if request.method == 'GET':
        # if g.user is None:
        #      msg ='로그인이 필요한 서비스입니다.'
        #      flash(msg)
        #      return redirect('/home')
        
        
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        rent_list = db.session.query(Rent, Books).filter(Rent.book_id == Books.id).filter(Rent.user_id == session.get('login')).filter(Rent.status == 1).all()
        
        #이렇게 조인을 하면, 첫번째는 Rent객체, 두번쨰는 Books 객체가 결과값으로 반환된다
        history = db.session.query(Rent, Books).filter(Rent.book_id == Books.id).filter(Rent.user_id == session.get('login')).all()

        if len(history) == 0: #대여 이력이 없을때
            return render_template('dashboard.html', cur_count = 0, total_count = 0 )

        cur_count = len(rent_list)
        total_count = db.session.query(func.count(Rent.user_id)).group_by(Rent.user_id).having(Rent.user_id == session.get('login')).first()[0]
        return render_template('dashboard.html', book_list = rent_list, cur_count = cur_count, total_count = total_count, history = history, today= today )
    elif request.method == 'POST':
        book_id = int(request.form.get('book_id'))
        book = Books.query.filter(Books.id == book_id).first()
        book.stock += 1
        db.session.commit()
        
        rented_book = Rent.query.filter((Rent.user_id == session.get('login'))& (Rent.status == 1)).all()
        for rent in rented_book:
            if rent.book_id == book_id:
                rent.status = 0
                rent.return_date = datetime.datetime.now()
                db.session.commit()
                break
        
        return jsonify({'result':'success'})