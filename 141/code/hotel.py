from dataclasses import dataclass

@dataclass(frozen=True)
class Hotel:
    name: str
	rooms: list
	location: str

@dataclass(frozen=True)
class Room:
    number: int
	capacity: int
	price: float

