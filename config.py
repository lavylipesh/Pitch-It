class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://lilibeth:1234@localhost/pitch'
    SECRET_KEY = '2wnd56mdj6hcmnc7cxn'
    UPLOADED_PHOTOS_DEST ='app/static/photos'