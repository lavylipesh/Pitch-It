from flask import Flask 
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

  


db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app,photos)
    mail.init_app(app)
   
    return app


