from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from routes import init_app

    init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
