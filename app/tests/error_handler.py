from flask import Flask, Blueprint
from flask import Flask, Blueprint, render_template, jsonify, session, request, g, redirect, url_for


bp = Blueprint('error_handler', __name__)
'''
“500 Internal Server Error” (InternalServerError) 

The good old “chap, you made a mistake typing that URL” message. So common that even novices to the internet know that 404 means: damn, the thing I was looking for is not there. It’s a very good idea to make sure there is actually something useful on a 404 page, at least a link back to the index.
410 Gone
Did you know that there the “404 Not Found” has a brother named “410 Gone”? Few people actually implement that, but the idea is that resources that previously existed and got deleted answer with 410 instead of 404. If you are not deleting documents permanently from the database but just mark them as deleted, do the user a favour and use the 410 code instead and display a message that what they were looking for was deleted for all eternity.
500 Internal Server Error
Usually happens on programming errors or if the server is overloaded. A terribly good idea is to have a nice page there, because your application will fail sooner or later (see also: Application Errors).
'''
@bp.app_errorhandler(403)
#Forbidden
#If you have some kind of access control on your website, you will have to send a 403 code for disallowed resources. So make sure the user is not lost when they try to access a forbidden resource.
def page_not_found(e):
    return render_template('error.html', error_msg = e), 403

@bp.app_errorhandler(404)
#Not Found
#The good old “chap, you made a mistake typing that URL” message. So common that even novices to the internet know that 404 means: damn, the thing I was looking for is not there. It’s a very good idea to make sure there is actually something useful on a 404 page, at least a link back to the index.
def page_not_found(e):
    return render_template('error.html', error_msg = e), 404

@bp.app_errorhandler(405)
#Method Not Allowed
def method_not_allowed(e):
    return render_template('error.html', error_msg = e), 405

@bp.app_errorhandler(500)
#Internal Server Error
#Usually happens on programming errors or if the server is overloaded. A terribly good idea is to have a nice page there, because your application will fail sooner or later (see also: Application Errors).
def internal_server(e):
    return render_template('error.html', error_msg = e), 500

