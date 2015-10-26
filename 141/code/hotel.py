#!/usr/bin/python
from rit_lib import *

class Hotel( struct ):
	_slots = ( (str,"name"), (list,"rooms"), (str,"location") )

def createHotel(name, rooms, location):
	return Hotel(name, rooms, location)

class Room( struct ):
	_slots = ( (int,"number"), (int,"capacity"), (float,"price") )

def createRoom(number, capacity, price):
	return Room(number, capacity, price)
