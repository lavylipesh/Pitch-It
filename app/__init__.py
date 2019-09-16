from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import Login_Manager


app = Flask(__name__)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



def create_app(config_name):
    
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
    return app