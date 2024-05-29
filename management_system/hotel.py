from operations import ReservationOperations
from utils.validators import validate_type
from rooms import Room
from guest import Guest
from datetime import datetime
from reservation import Reservation


class Hotel(ReservationOperations):
    def __init__(self) -> None:
        self.__rooms = []
        self.__guests = []

    def add_room(self, room: Room) -> None:
        validate_type(room, Room)
        self.__rooms.append(room)

    def add_guest(self, guest: Guest) -> None:
        validate_type(guest, Guest)
        self.__guests.append(guest)

    def search_available_room(self) -> list:
        res = []
        for room in self.__rooms:
            if room.is_available:
                res.append(room)
        return res

    def book_room(self, guest: Guest, number: int, date: datetime) -> None:
        validate_type(guest, Guest)
        for room in self.__rooms:
            if room.number == number:
                if room.is_available:
                    room.is_available = False
                    reservation = Reservation(guest, room, date)
                    guest.reservation_history.append(reservation)
