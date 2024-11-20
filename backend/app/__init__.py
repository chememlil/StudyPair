from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    CORS(app)

    # Register blueprints
    from app.student import student
    from app.pairing import pairing
    from app.history import history
    from app.auth import auth

    app.register_blueprint(student, url_prefix='/students')
    app.register_blueprint(pairing, url_prefix='/pairing')
    app.register_blueprint(history, url_prefix='/history')
    app.register_blueprint(auth, url_prefix='/auth')

    return app
