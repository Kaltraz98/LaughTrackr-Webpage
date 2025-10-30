from flask import Blueprint, render_template, request, redirect, url_for
from .models import *
from .eventforms import *
from laughtrackr import db
from flask_login import login_required 

# Create blueprint
eventsbp = Blueprint('events', __name__, url_prefix='/events')

# Homepage carousel view
@eventsbp.route('/homepage')
def carousel():
    events = Event.query.filter(Event.id.in_([1, 2, 3])).all()
    return render_template('IndexPage.html', events=events)

# All events listing
@eventsbp.route('/all')
def all_events():
    events = Event.query.all()
    return render_template('AllEventsPage.html', events=events)

# Event details view
@eventsbp.route('/details/<int:id>', methods=['GET', 'POST'])
def events(id):
    event = Event.query.get_or_404(id)
    return render_template('EventDetailsPage.html', event=event)

# Event creation form
@eventsbp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    print('Method type:', request.method)
    create_form = EventForm()
    create_form.rating.choices = [(r.id, r.label) for r in Rating.query.all()]
    create_form.venue.choices = [(v.id, v.name) for v in Venue.query.all()]

    if create_form.validate_on_submit():
        new_event = Event(
            name=create_form.name.data,
            description=create_form.description.data,
            image=create_form.image.data,
            cost=create_form.cost.data,
            rating_id=create_form.rating.data,
            venue_id=create_form.venue.data,
            event_date=create_form.event_date.data
        )
        db.session.add(new_event)
        db.session.commit()
        print('Successfully created new comedy event')
        return redirect(url_for('events.details', id=new_event.id))

    return render_template('EventcreationPage.html', form=create_form)

# Utility function to fetch event by ID
def get_event(id):
    return Event.query.get(id)