# Imports
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from laughtrackr import db
from sqlalchemy import func

from .models import Event, Comment, Rating, Venue, Booking
from .eventforms import EventForm
from .Userforms import BookingForm, CommentForm

# Create blueprint
eventsbp = Blueprint('events', __name__, url_prefix='/events')
bookingbp = Blueprint('booking', __name__, url_prefix='/booking')

# Homepage carousel view
@eventsbp.route('/homepage')
def carousel():
    events = Event.query.filter(Event.id.in_([1, 2, 3])).all()

    fallon = Event.query.get(4)
    beast = Event.query.get(5)
    carr = Event.query.get(6)

    for e in [fallon, beast, carr]:
        if e and e.venue:
            booked = db.session.query(func.sum(Booking.quantity)).filter_by(event_id=e.id).scalar() or 0
            e.remaining_seats = e.venue.seating_capacity - booked

    return render_template('IndexPage.html', events=events, fallon=fallon, beast=beast, carr=carr)

# All events listing
@eventsbp.route('/all')
def all_events():
    events = Event.query.all()
    return render_template('AllEventsPage.html', events=events)

# Event details view with booking and comments
@eventsbp.route('/details/<int:id>', methods=['GET', 'POST'])
@login_required
def event_details(id):
    event = Event.query.get_or_404(id)
    form = BookingForm()
    comment_form = CommentForm()

    # Calculate remaining seats
    booked = db.session.query(func.sum(Booking.quantity)).filter_by(event_id=event.id).scalar() or 0
    seats_available = event.venue.seating_capacity - booked

    if comment_form.validate_on_submit():
        new_comment = Comment(
            text=comment_form.text.data,
            user_id=current_user.id,
            event_id=event.id
        )
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment posted!', 'success')
        return redirect(url_for('events.event_details', id=event.id))

    comments = Comment.query.filter_by(event_id=event.id).order_by(Comment.created_at.desc()).all()

    return render_template(
        'EventDetailsPage.html',
        event=event,
        form=form,
        comment_form=comment_form,
        comments=comments,
        seats_available=seats_available 
    )

# Event creation form
@eventsbp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
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
            event_date=create_form.event_date.data,
            user_id=current_user.id  # Link to creator
        )
        db.session.add(new_event)
        db.session.commit()
        flash('Successfully created new comedy event!', 'success')
        return redirect(url_for('events.event_details', id=new_event.id))

    return render_template('EventcreationPage.html', form=create_form)

# Utility function - get ID
def get_event(id):
    return Event.query.get(id)

# User created events
@eventsbp.route('/my-events')
@login_required
def my_events():
    user_events = Event.query.filter_by(user_id=current_user.id).all()
    return render_template('MyEventsPage.html', events=user_events)

@bookingbp.route('/book/<int:event_id>', methods=['POST'])
@login_required
def book_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = BookingForm()

    # Dynamically calculate remaining seats
    booked = db.session.query(func.sum(Booking.quantity)).filter_by(event_id=event.id).scalar() or 0
    remaining_seats = event.venue.seating_capacity - booked

    if form.validate_on_submit():
        quantity = form.quantity.data
        if quantity > remaining_seats:
            flash(f"Only {remaining_seats} seats are available. Please select a lower quantity.", "danger")
            return redirect(url_for('events.event_details', id=event_id))

        # Proceed with booking
        new_booking = Booking(
            user_id=current_user.id,
            event_id=event.id,
            quantity=quantity
        )
        db.session.add(new_booking)
        db.session.commit()

        flash("Tickets successfully booked!", "success")
        return redirect(url_for('events.event_details', id=event_id))

    flash("There was an error with your submission.", "danger")
    return redirect(url_for('events.event_details', id=event_id))