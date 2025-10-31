from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField, DateTimeField, FloatField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileField, FileAllowed

# Allowed image file extensions
ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

class EventForm(FlaskForm):
    name = StringField('Name of the Event', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        # Uncomment these if image upload should be required
        # FileRequired(message='Image cannot be empty'),
        # FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, JPEG')
    ])
    cost = FloatField('Cost', validators=[InputRequired()])
    rating = SelectField('Rating', coerce=int, validators=[InputRequired()])
    venue = SelectField('Venue', coerce=int, validators=[InputRequired()])
    event_date = DateTimeField('Event Date', format='%Y-%m-%dT%H:%M', validators=[InputRequired()])
    submit = SubmitField("Create")

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