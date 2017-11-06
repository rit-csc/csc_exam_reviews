from rit_lib import *

Hotel = struct_type("Hotel",
	(str, "name"), (list, "rooms"), (str, "location"))

Room = struct_type("Room",
	(int, "number"), (int, "capacity"), (float, "price"))
