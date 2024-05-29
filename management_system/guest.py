from __future__ import annotations
from utils.validators import String, Email, validate_type


class Guest:
    name = String()
    contact_info = Email()

    def __init__(self, name: str, contact_info: str) -> None:
        self.name = name
        self.contact_info = contact_info
        self.reservation_history = []

    def view_reservation_history(self) -> None:
        for reservation in self.reservation_history:
            print(reservation)

    def leave_feedback(self, reservation: Reservation, feedback: str) -> None:
        if reservation in self.reservation_history:
            validate_type(feedback, str)
            reservation.feedback = feedback


from reservation import Reservation
