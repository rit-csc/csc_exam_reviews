from rit_lib import *

class WonkyHashTable( struct ):
	_slots = ( (int,"size"), (list,"table") )

def createWonkyHashTable(size=4):
	table = [[] for i in range(size)]
	return WonkyHashTable(size, table)

def add_element(wonkyHashTable, element):
	hash = bad_hash(wonkyHashTable, element)
	wonkyHashTable.table[hash] = element

def contains(wonkyHashTable, element):
	for t in wonkyHashTable.table:
		if element in t:
			return True
		return False

def bad_hash(wonkyHashTable, element):
	return len(element) % len(wonkyHashTable.table)

# main program

htable = createWonkyHashTable()
for elm in 'I wrestled a bear once'.split():
    add_element(htable, elm)
