from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event, Venue, Rating
from .eventforms import EventForm
from .NewEvent import *
from laughtrackr import db

destbp = Blueprint('events', __name__, url_prefix='/events')

@destbp.route('/<id>')
def show(id):
    event = get_event(id)
    return render_template('ComedyEvent/show.html', event=event)

@destbp.route('/create', methods=['GET', 'POST'])
def create():
    print('Method type: ', request.method)
    create_form = EventForm()
    #create_form.rating.choices = [(r.id, r.label) for r in Rating.query.all()]
    #create_form.venue.choices = [(v.id, v.name) for v in Venue.query.all()]
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
        return redirect(url_for('events.show', id=new_event.id))
    return render_template('EventcreationPage.html', form=create_form)

def get_event(id):
  return Event.query.get(id)