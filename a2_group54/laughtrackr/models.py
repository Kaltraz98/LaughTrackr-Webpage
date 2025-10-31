from . import db
from datetime import datetime
from flask_login import UserMixin

# User Model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # Encrypted password

    comments = db.relationship('Comment', backref='user', cascade='all, delete-orphan')
    events = db.relationship('Event', backref='user', cascade='all, delete-orphan')
    bookings = db.relationship('Booking', backref='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.name}>"

# Event Model
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(400))
    cost = db.Column(db.Float, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    event_addinfo = db.Column(db.String(500))
    featured = db.Column(db.Boolean, default=False)

    rating_id = db.Column(db.Integer, db.ForeignKey('rating.id'), nullable=False)
    rating = db.relationship('Rating', backref='event')

    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    venue = db.relationship('Venue', backref='events')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    comments = db.relationship('Comment', backref='event', lazy=True)
    bookings = db.relationship('Booking', backref='event', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Event {self.name} in {self.venue.name}>"

# Comment Model
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

    def __repr__(self):
        return f"<Comment by User {self.user_id} on Event {self.event_id}>"

# Booking Model
class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

    def __repr__(self):
        return f"<Booking User {self.user_id} Event {self.event_id} Quantity {self.quantity}>"

# Venue Model
class Venue(db.Model):
    __tablename__ = 'venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    seating_capacity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {column.name: str(getattr(self, column.name)) for column in self.__table__.columns}

# Rating Model
class Rating(db.Model):
    __tablename__ = 'rating'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Rating {self.id}: {self.label}>"