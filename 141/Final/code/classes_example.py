class Hotel:
		__slots__ = ("name", "rooms", "location")

def mkHotel(name, rooms, location):
	hotel = Hotel()
	hotel.name = name
	hotel.rooms = rooms # rooms = list containing Room objs
	hotel.location = location
	return hotel

class Room:
	__slots__=("number", "capacity", "price")

def mkRoom(number, capacity, price):
	room = Room()
	room.number = number
	room.capacity = capacity
	room.price = price
	return room


hotel = mkHotel("Chris", [], "Zimbabwe")

print(hotel.name)
print(hotel.rooms)
print(hotel.location)
