from flask import Blueprint, render_template

#Blueprint and root URL
destbp = Blueprint('BookingHistory', __name__, url_prefix='/booking-history')

@destbp.route('/<id>')
def show(id):
    return render_template('UserBookingHistoryPage.html')
