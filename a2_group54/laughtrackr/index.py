from flask import Blueprint, render_template
from sqlalchemy import func
from .models import Event, Booking
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    # Carousel events
    events = Event.query.filter(Event.id.in_([1, 2, 3])).all()

    # Featured events
    fallon = Event.query.get(4)
    beast = Event.query.get(5)
    carr = Event.query.get(6)

    # Annotate remaining seats
    for e in [fallon, beast, carr]:
        if e and e.venue:
            booked = db.session.query(func.sum(Booking.quantity)).filter_by(event_id=e.id).scalar() or 0
            e.remaining_seats = e.venue.seating_capacity - booked
    
    fallon = Event.query.get(4) or Event(name="Jimmy Fallon", description="Coming soon", image="default.jpg", venue=None)

    return render_template('IndexPage.html', events=events, fallon=fallon, beast=beast, carr=carr)