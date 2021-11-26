from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for
from app import db
from app.models import Users, Books
from flask_bcrypt import Bcrypt
import re

bp = Blueprint("auth", __name__, url_prefix="/user")
bcrypt = Bcrypt()

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('login')
    if user_id is None:
        g.user = None
    else:
        g.user = Users.query.filter(Users.id == user_id).first()

@bp.route('/login', methods=['POST', 'GET'])
def login():
    if session.get('login') is None:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            user_id = request.form.get('user_id')
            user_pw = request.form.get('user_pw')
            if len(user_pw) < 8: 
                return jsonify({'result':'pw_length'})

            user = Users.query.filter(Users.user_id == user_id).first()

            if user is None:
                return jsonify({'result':'none user'})
            else:
                if bcrypt.check_password_hash(user.pw_hash, user_pw):
                    session['login'] = user.id
                    return jsonify({"result": "success", 'name':user.name})
                else:
                    return jsonify({'result':'fail'})
    else:
        redirect('/home')

                    
@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/home')

@bp.route('/signup', methods=['POST','GET'])
def signup():
    if session.get('login') is None:
        name_regex = r'^[가-힣a-zA-Z]{2,10}$'
        email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$'
        pw_regex = r'^(?!.* )(?=.*[a-zA-Z])(?=.*[~!@#$%^&*()_+|<>?:{}])(?=.*[0-9]).{8,16}$'

        if request.method == 'POST':
            user_id = request.form['user_email']
            user_pw1 = request.form['user_pw1']
            user_pw2 = request.form['user_pw2']
            user_name = request.form['user_name']
            
            if not re.search(name_regex, user_name):
                return jsonify({'result':'check_name'})
            if not re.search(email_regex, user_id):
                return jsonify({'result':'check_email'})
            if not re.search(pw_regex, user_pw1) or not re.search(pw_regex, user_pw2):
                return jsonify({'result':'check_pw'})    
            if user_pw1 != user_pw2:
                return jsonify({'result':'check_pw'})
            

            data = Users.query.filter(Users.user_id == user_id).first()
            if data is not None:
                return jsonify({'result':'check_id'})
            else:
                pw_hash = bcrypt.generate_password_hash(user_pw2).decode()
                user = Users(user_id, pw_hash, user_name)
                db.session.add(user)
                db.session.commit()
                return jsonify({'result':'success'})
        return render_template('signup.html')   
    else:
        return redirect('/home')
            


