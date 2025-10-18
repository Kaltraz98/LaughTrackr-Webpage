from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)
    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')

    # string print method
    def __repr__(self):
        return f"Name: {self.name}"

class Event(db.Model):
    __tablename__ = 'Events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    cost = db.Column(db.String(3))
    #Relationships
    rating = db.relationship('Rating', backref='event')
    rating_id = db.Column(db.Integer, db.ForeignKey('rating.id'))
    comments = db.relationship('Comment', backref='event')
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))
    event_date = db.Column(db.DateTime, nullable=False)
	# string print method
    def __repr__(self):
        return f"Name: {self.name}"

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    def __repr__(self):
        return f"Comment: {self.text}"
    
class Venue(db.Model):
    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    seating_capacity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        h_dict = {
            b.name: str(getattr(self, b.name)) for b in self.__table__.columns
        }
        return h_dict

class rating(db.Model):
    __tablename__ = 'Rating'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Rating {self.id}: {self.label}>"