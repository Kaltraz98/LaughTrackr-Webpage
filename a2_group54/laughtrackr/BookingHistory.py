from flask import Blueprint, render_template

#Blueprint and root URL
bookingbp = Blueprint('Booking', __name__, url_prefix='/booking-history')

@bookingbp.route('/<id>')
def showhistory(id):
    return render_template('UserBookingHistoryPage.html')
