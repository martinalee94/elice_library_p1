import os

from config import config
from dotenv import load_dotenv
from flask import Flask, redirect
from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ["APP_KEY"]
    config_type = os.getenv("FLASK_ENV") if os.getenv("FLASK_ENV") else "default"
    app.config.from_object(config[config_type])
    config[config_type].init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    from . import auth

    app.register_blueprint(auth.bp)

    from . import main

    app.register_blueprint(main.bp)

    from . import detail

    app.register_blueprint(detail.bp)

    from . import dashboard

    app.register_blueprint(dashboard.bp)

    from .tests import error_handler

    app.register_blueprint(error_handler.bp)

    @app.route("/")
    def welcome():
        return redirect("/home/")

    # TODO: ModelView 추가시 에러 발생, fix필요
    admin = Admin(app, name="Admin", template_mode="bootstrap3")
    return app


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

if __name__ == "__main__":
    load_dotenv(dotenv_path)
    app = create_app()

    if os.environ["MODE"] == 1:
        app.run("0.0.0.0", 80)
    else:
        app.run("127.0.0.1", 5000)
