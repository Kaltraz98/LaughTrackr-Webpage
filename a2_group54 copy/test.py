from datetime import datetime
from events.user import User
from events.user import FrequentPatron
from events.event import Booking
from events.location import Location

print('Creating a user named Macron')
user = User()
user.register('Macron','pass123','emmanual@google.com')
print(user)

print('################')

print('Creating a frequent patron named Jimmy')
freq_user = FrequentPatron()
freq_user.register('Jimmy','pass123', 'thebeast@google.com', 123231)
print(freq_user)

print('###############')

print('Creating a location Brisbane')
brisbane = Location('Brisbane', 'City in Queensland with good weather')
print(brisbane)

start_date = datetime(2024,11,23,10,0,0)
start_time = datetime(2024,11,30,10,0,0)

print('Creating a booking for user')
booking = Booking(start_date, start_time, brisbane, user)
print('#################')
print(booking)

print('#################')
print("Access City description of Booking: ", booking.location.description)