from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for
from app import db
from app.models import Users, Books

bp = Blueprint("detail", __name__, url_prefix="/books/detail")


@bp.route('/<isbn>')
def detail(isbn):
    book = Books.query.filter(Books.isbn == isbn).first()
    return render_template('detail.html', book = book)