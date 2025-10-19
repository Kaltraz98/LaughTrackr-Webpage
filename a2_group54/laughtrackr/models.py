from . import db
from datetime import datetime
from flask_login import UserMixin

# Create User DB
class User(db.Model, UserMixin):
    __tablename__ = 'users' # table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, unique=True, nullable=False)
	# encrypted password must be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)
    # relation to comments = Many to many 
    comments = db.relationship('Comment', backref='user', cascade='all, delete-orphan')

    # string print
    def __repr__(self):
       return f"<User {self.name}>"

# Create Event DB
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    cost = db.Column(db.float)
    # Foriegn Keys
    rating = db.relationship('Rating', backref='event')
    rating_id = db.Column(db.Integer, db.ForeignKey('rating.id'))
    comments = db.relationship('Comment', backref='event', lazy=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    venue = db.relationship('Venue', backref='events')
    event_date = db.Column(db.DateTime, nullable=False)
    
	# string print 
    def __repr__(self):
        return f"<event {self.name} in {self.venue}>"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    

    
class Venue(db.Model):
    __tablename__ = 'venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    seating_capacity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(300), nullable=False)


    def to_dict(self):
        h_dict = {
            b.name: str(getattr(self, b.name)) for b in self.__table__.columns
        }
        return h_dict

class Rating(db.Model):
    __tablename__ = 'rating'
    rating = db.relationship('Rating', backref='event')
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<rating {self.id}: {self.label}>"
    
   