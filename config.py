import os

class Config:
    
    # SQLALCHEMY_DATABASE_URI='postgres+psycopg2://lilibeth:1234@127.0.0.1:5432/pitches'
    SECRET_KEY='2wnd56mdj6hcmnc7cxn'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'


   
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")    

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}