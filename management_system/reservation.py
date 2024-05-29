from __future__ import annotations
from utils.validators import DateTime
from datetime import datetime


class Reservation:
    date = DateTime()

    def __init__(self, guest: Guest, room: Room, date: datetime) -> None:
        self.guest = guest
        self.room = room
        self.date = date
        self.feedback = None

    def __str__(self) -> str:
        return (f'Reservation for {self.guest} in room {self.room.number} for '
                f'{self.date}. ')


from guest import Guest
from rooms import Room
