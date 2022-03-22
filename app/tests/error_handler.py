from flask import Blueprint, render_template

bp = Blueprint("error_handler", __name__)


@bp.app_errorhandler(403)
def forbidden(e):
    e = e.split(":")[0]
    return render_template("error.html", error_msg=e), 403


@bp.app_errorhandler(404)
def page_not_found(e):
    e = str(e).split(":")[0]
    return render_template("error.html", error_msg=e), 404


@bp.app_errorhandler(405)
def method_not_allowed(e):
    e = str(e).split(":")[0]
    return render_template("error.html", error_msg=e), 405


@bp.app_errorhandler(408)
def request_timeout(e):
    e = str(e).split(":")[0]
    return render_template("error.html", error_msg=e), 408


@bp.app_errorhandler(500)
def internal_server(e):
    e = str(e).split(":")[0]
    return render_template("error.html", error_msg=e), 500


@bp.app_errorhandler(ValueError)
def value_error(e):
    e = str(e).split(":")[0]
    return render_template("error.html", error_msg=e), 500
