from flask import render_template
from .models import Event  # adjust import as needed
from . import eventsbp  # your blueprint

@eventsbp.route('/featured')
def show_featured_events():
    featured_names = ["Aunty Donna", "Daniel Sloss", "James Acaster"]
    highlighted_events = Event.query.filter(Event.name.in_(featured_names)).all()
    return render_template("your_template.html", events=highlighted_events)