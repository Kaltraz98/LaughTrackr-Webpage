from flask import Blueprint, render_template
from .models import *
from . import db

mainbp = Blueprint('main', __name__)  

@mainbp.route('/')
def index():
    events = Event.query.all()
    for event in events:
        event.image = event.image.strip()
    db.session.commit()
    return render_template('IndexPage.html', events=events)