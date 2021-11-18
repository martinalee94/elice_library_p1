from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for
#from app import db
#from models import Users, Books


bp = Blueprint("auth", __name__, url_prefix="/user")

@bp.route('/login', methods=['POST', 'GET'])
def hi():
    return 'heyhey'
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     if request.method == 'POST':
#         user_id = request.form['user_id']
#         user_pw = request.form['user_pw']
#         user = Users.query.filter(Users.user_id == user_id).first()
#         if user is None:
#             return jsonify({'result':'check_id'})
#         else:
#             return jsonify({'result':'success'})

# def logout():
# def join():
