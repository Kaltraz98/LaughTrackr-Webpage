from datetime import datetime
from .user import User

class Booking:

    def __init__(self, startdate, starttime, location, user):
        self.startdate = startdate
        self.starttime = starttime
        self.location = location
        self.user = user
        self.num_tickets = 1
    
    def __repr__(self):
        str = f"User: {self.user}\nCity: {self.location.name}\nStart date: {self.startdate}\nEnd date: {self.starttime}\nNumber of tickets: {self.num_tickets}"
        return str