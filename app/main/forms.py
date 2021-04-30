from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo,DataRequired
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you.',validators = [Required()])
  submit = SubmitField('Submit')

class PostForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  content = TextAreaField('Content', validators=[DataRequired()])
  submit = SubmitField('Post')

class UpdatePostForm(FlaskForm):
  title = StringField("Blog title", validators=[Required()])
  post = TextAreaField("Type Away", validators=[Required()])
  submit = SubmitField("Update")