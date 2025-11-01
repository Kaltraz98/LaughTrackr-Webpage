# Imports
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    FloatField,
    SelectField,
    DateTimeField,
    SubmitField
)
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

# Allowed image file extensions
ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

# Event creation form
class EventForm(FlaskForm):
    name = StringField('Name of the Event', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Event Image', validators=[
    ])
    cost = FloatField('Cost', validators=[InputRequired()])
    rating = SelectField('Rating', coerce=int, validators=[InputRequired()])
    venue = SelectField('Venue', coerce=int, validators=[InputRequired()])
    event_date = DateTimeField('Event Date', format='%Y-%m-%dT%H:%M', validators=[InputRequired()])
    submit = SubmitField("Create")

# Event details form 
class Details_Form(FlaskForm):
    name = StringField('Name of the Event', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, JPEG')
    ])
    cost = FloatField('Cost', validators=[InputRequired()])
    rating = SelectField('Rating', coerce=int, validators=[InputRequired()])
    venue = SelectField('Venue', coerce=int, validators=[InputRequired()])
    event_date = DateTimeField('Event Date', format='%Y-%m-%dT%H:%M', validators=[InputRequired()])
    submit = SubmitField("Create")