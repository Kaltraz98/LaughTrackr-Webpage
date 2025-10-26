from flask import Blueprint, render_template, request, redirect, url_for
from .models import *
from .eventforms import *
from laughtrackr import db

eventsbp = Blueprint('events', __name__, url_prefix='/events')

@eventsbp('/events')
def all_events():
    events = Event.query.all()
    return render_template('AllEventsPage.html', events=events)

@eventsbp.route('/details/<int:id>', methods=['GET', 'POST'])
def events(id):
    event = Event.query.get_or_404(id)
    return render_template('EventDetailsPage.html', event=event)

@eventsbp.route('/create', methods=['GET', 'POST'])
def create():
    print('Method type: ', request.method)
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

def get_event(id):
  return Event.query.get(id)

events = [
    Event(id=1, name="Aunty Donna", description="DREM Worldwide Tour", image_path="img_folder/Aunty_Donna.jpg"),
    Event(id=2, name="Daniel Sloss", description="BITTER Australia Tour", image_path="img_folder/Daniel_Sloss.jpg"),
    Event(id=3, name="James Acaster", description="Hecklers Welcome", image_path="img_folder/James_Acastor.jpg")
]