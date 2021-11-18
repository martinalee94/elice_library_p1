from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for
from app import db
from app.models import Users, Books

bp = Blueprint("books", __name__, url_prefix="/")

@bp.route('/home')
def home():
    book_list = Books.query.all()
    return render_template('home.html', book_list = book_list)