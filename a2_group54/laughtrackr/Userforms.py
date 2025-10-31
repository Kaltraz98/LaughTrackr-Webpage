# Imports
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    SubmitField,
    IntegerField,
    SelectField
)
from wtforms.validators import InputRequired, Email, EqualTo, NumberRange

# Allowed image file extensions
ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

# User login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

# User registration form
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            InputRequired(),
            EqualTo('password', message='Passwords must match')
        ]
    )
    submit = SubmitField('Register')

# User comment form
class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment', validators=[InputRequired()])
    submit = SubmitField('Post')

# Ticket booking form
class BookingForm(FlaskForm):
    quantity = SelectField(
        'Number of Tickets',
        choices=[(str(i), str(i)) for i in range(1, 7)],
        validators=[InputRequired()]
    )
    submit = SubmitField('Purchase')