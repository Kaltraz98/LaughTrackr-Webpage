from laughtrackr import db, create_app
from laughtrackr.models import *
app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()

#Add Venue
Palis = Venue(name="Palais Theatre", address="St Kilda, VIC", seating_capacity=2896)
db.session.add(Palis)
Tivoli = Venue(name="Tivoli", address="Fortitude Valley, QLD", seating_capacity=1)
db.session.add(Tivoli)
db.session.commit()

#Ratings
rating_labels = ["G", "PG", "M", "MA15+", "R18+"]
for label in rating_labels:
    if not Rating.query.filter_by(label=label).first():
        db.session.add(Rating(label=label))

# Create new event
AuntyDonna = Event(
    name="DREM International Tour",
    description="Aunty Donna's new live sketch show — wild, hilarious, and unforgettable.",
    image="img_folder/DREMTOUR.png",  
    cost="45",  
    rating_id=1,
    venue_id=1,
    event_date=datetime(2025, 12, 13, 20, 0) , 
    event_addinfo ="https://www.auntydonna.com/"
)
JimmyBeast = Event(
    name="DJ BEAST",
    description="TAG LINE",
    image="img_folder/JimmyBeast.jpg",  
    cost="4500",  
    rating_id=4,
    venue_id=2,
    event_date=datetime(2025, 12, 13, 20, 0) , 
    event_addinfo ="CHECK OUT JIMMY BEAST"
)
db.session.add(AuntyDonna)
db.session.add(JimmyBeast)
db.session.commit()

quit()