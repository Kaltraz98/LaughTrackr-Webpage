from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from wtforms import SelectField

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}
    
#User login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

#User register
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        InputRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

#User comment
class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment', validators=[InputRequired()])
    submit = SubmitField('Post')

class BookingForm(FlaskForm):
    quantity = IntegerField('Number of Tickets', validators=[InputRequired(), NumberRange(min=1, max=6)])
    submit = SubmitField('Purchase')

class BookingForm(FlaskForm):
    quantity = SelectField('Number of Tickets', choices=[(str(i), str(i)) for i in range(1, 7)], validators=[InputRequired()])
    submit = SubmitField('Purchase')