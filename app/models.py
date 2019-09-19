from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments = db.relationship('Comments',backref = 'user',lazy = "dynamic")
    pitch = db.relationship('Pitch',backref ='user',lazy = "dynamic")
    pass_secure = db.Column(db.String(255))
   
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)    
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User{self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    pitch= db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comments',backref='pitch' ,lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_pitch(cls):
        pitches = Pitches.query.all()
        
        def __repr__(self):
            return f'Pitch{self.pitch}'


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    comments = db.Column(db.String(255))
    author = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls):
        comments = Comments.query.all()

        def __repr__(self):
            return f'Comments{self.comments}'

