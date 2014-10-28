#!/usr/bin/python

class Hotel :
	__slots__=("number", "capacity", "price")

def mkHotel(name, rooms , location ):
	hotel = Hotel()
	hotel.name = name
	hotel.rooms = rooms # a list containing Room objects
	hotel.location = location
	return hotel 

class Room:
	__slots__=("number" , "capacity" , "price")

def mkRoom(number, capacity, price):
	room = Room()
	room.number = number
	room.capacity = capacity
	room.price = price
	return room

