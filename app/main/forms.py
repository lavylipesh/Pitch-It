from  flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
  pass 

class PitchForm(FlaskForm):
  title = StringField('Title',validators=[Required()])
  pitch = TextAreaField('Write a pitch',validators=[Required()])
  submit = SubmitField('submit')

class CommentForm(FlaskForm):
  comments = TextAreaField('Your comment here',validators=[Required()])
  author = StringField('Author',validators=[Required()])
  submit = SubmitField('submit')