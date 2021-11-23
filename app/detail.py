from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for
from app import db
from app.models import Users, Books, Rating
import requests

bp = Blueprint("detail", __name__, url_prefix="/books/detail")


@bp.route('/<id>', methods=['GET', 'POST', 'DELETE'])
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
                rating = int(request.form.get('rating'))
                book_id = int(request.form.get('book_id'))
                user_id = session['login']
                new_review = Rating(user_id, book_id, rating, review)
                db.session.add(new_review)
                db.session.commit()

                book = Books.query.filter(Books.id == book_id).first()
                #review_list = db.session.query(Rating, Users).filter(Rating.user_id == Users.id).filter(Rating.book_id == book_id).order_by(Rating.created_date.desc()).all()
                #review_try1 = db.session.query(Rating).join(Users, Rating.user_id == Users.id).all()
                #review_try2 = db.session.query(Rating).join(Users).all()
                review_db = Rating.query.order_by(Rating.created_date.desc()).all()
                user_db = Users.query.all()
                
                user_list = []
                review_list = []

                for u in user_db: #user 리스트 만들기
                    user_list.append({'id': u.id, 'name':u.name})

                for r in review_db: #review 리스트 만들기
                    if r.book_id == book_id:
                        for user in user_list:
                            if user['id'] == r.user_id:
                                user_name = user['name']
                                break
                                
                        review_list.append({
                            'user_id':r.user_id,
                            'user_name': user_name,
                            'book_id':r.book_id, 
                            'created_date':r.created_date.strftime("%Y-%m-%d"), 
                            'description': r.description}
                        )
                return jsonify(review_list = review_list)
            except:
                return jsonify({'result':'duplicated'})
 
    elif request.method == 'DELETE':
        if session.get('login') is None:
            return jsonify({'result':'no session'})
        else:
            try:
                book_id = int(request.args.get('book'))
                user_id = session['login']

                Rating.query.filter((Rating.user_id == user_id) & (Rating.book_id == book_id)).delete()
                db.session.commit()
                review_db = Rating.query.order_by(Rating.created_date.desc()).all()
                user_db = Users.query.all()
                
                user_list = []
                review_list = []

                for u in user_db: #user 리스트 만들기
                    user_list.append({'id': u.id, 'name':u.name})

                for r in review_db: #review 리스트 만들기
                    if r.book_id == book_id:
                        for user in user_list:
                            if user['id'] == r.user_id:
                                user_name = user['name']
                                break

                        review_list.append({ 
                            'user_id':r.user_id,
                            'user_name': user_name,
                            'book_id':r.book_id, 
                            'created_date':r.created_date.strftime("%Y-%m-%d"), 
                            'description': r.description}
                        )
                return jsonify(review_list = review_list)
            except:
                return jsonify({'result':'fail'})