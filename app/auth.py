from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for
from app import db
from app.models import Users, Books
from flask_bcrypt import Bcrypt


bp = Blueprint("auth", __name__, url_prefix="/user")
bcrypt = Bcrypt()

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('login')
    if login is None:
        g.user = None
    else:
        g.user = Users.query.filter(Users.user_id == user_id).first()

@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user_id = request.form.get('id')
        user_pw = request.form.get('pw')

        if len(user_pw) < 8:
            return jsonify({'result':'pw_length'})

        user = Users.query.filter(Users.user_id == user_id).first()

        if user is None:
            return jsonify({'result':'fail'})
        else:
            if bcrypt.check_password_hash(user.pw_hash, user_pw):
                session['login'] = user.id
                return jsonify({"result": "success"})
            else:
                return jsonify({'result':'fail'})

                    
@bp.route('/logout')
def logout():
    session['login'] = None
    return redirect('/home')

@bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')   
    elif request.method == 'POST':
        user_id = request.form.get('user_id')
        user_pw1 = request.form.get('user_pw1')
        user_pw2 = request.form.get('user_pw2')
        name = request.form.get('name')

        if user_pw1 != user_pw2:
            return jsonify({'result':'check_pw'})
        
        if len(user_pw1) < 8 or len(user_pw2) < 8:
            return jsonify({'result':'pw_length'})
        
        data = Users.query.filter(Users.user_id == user_id).first()
        if data is not None:
            return jsonify({'result':'check_id'})
        else:
            pw_hash = bcrypt.generate_password_hash(user_pw2).decode()
            user = Users(user_id, pw_hash, name)
            db.session.add(user)
            db.session.commit()
            return jsonify({'result':'success'})
            


