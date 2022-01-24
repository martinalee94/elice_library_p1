import os

import config
from flask import Flask, redirect, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# db 객체를 create_app 함수 안에서 생성하면 블루프린트와 같은 다른 모듈에서 불러올 수  없음
# db, migrate와 같은 객체를 create_app 함수 밖에서 생성
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = os.environ["APP_KEY"]
    # ORM 실제 객체 초기화는 create_app 함수에서 init_app 함수를 통해 진행
    db.init_app(app)
    migrate.init_app(app, db)
    from . import auth, models

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

    return app


if __name__ == "__main__":
    app = create_app()
    if os.environ["MODE"] == 1:
        app.run("0.0.0.0", 80, debug=False)
    else:
        app.run("127.0.0.1", 5000, debug=True)
