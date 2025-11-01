# Imports
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Booking, Event, Comment
from .Userforms import BookingForm, CommentForm
from . import db

# Define blueprint
bookingbp = Blueprint('booking', __name__, url_prefix='/booking')

# Booking history route
@bookingbp.route('/history')
@login_required
def showhistory():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('bookings.html', bookings=bookings)

# Booking form route
@bookingbp.route('/event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def book_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = BookingForm()
    comment_form = CommentForm()  # ✅ Corrected name
    
    if form.validate_on_submit():
        total_booked = sum(b.quantity for b in Booking.query.filter_by(event_id=event.id).all())
        remaining_seats = event.venue.seating_capacity - total_booked

        if int(form.quantity.data) > remaining_seats:
            flash(f'Only {remaining_seats} tickets left for this event.', 'danger')
            return render_template('EventDetailsPage.html', event=event, form=form, comment_form=comment_form)

        booking = Booking(
            user_id=current_user.id,
            event_id=event.id,
            quantity=int(form.quantity.data)
        )
        db.session.add(booking)
        db.session.commit()

        flash(f'You successfully booked {form.quantity.data} ticket(s) for "{event.name}"!', 'success')
        return redirect(url_for('booking.showhistory'))

    return render_template('EventDetailsPage.html', event=event, form=form, comment_form=comment_form)