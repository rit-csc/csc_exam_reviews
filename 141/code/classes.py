#!/usr/bin/python
from rit_object import *

class Hotel(rit_object) :
	_slots=("name", "rooms", "location")
	_types=(str, list, str)

def mkHotel(name, rooms , location ):
	hotel = Hotel()
	hotel.name = name
	hotel.rooms = rooms # a list containing Room objects
	hotel.location = location
	return hotel 

class Room(rit_object):
	_slots=("number" , "capacity" , "price")
	_types=(int, int, float)

def mkRoom(number, capacity, price):
	room = Room()
	room.number = number
	room.capacity = capacity
	room.price = price
	return room

