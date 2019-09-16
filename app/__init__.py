from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy(app)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app