from __future__ import annotations
from operations import DriverOperations
from utils.validators import String, Email, validate_type
from vehicles import Vehicle


class Driver(DriverOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str,
            vehicle: Vehicle
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.vehicle = vehicle
        self.requested_rides = []
        self.rides = []
        self.completed_rides = []
        self.ratings = []

    def accept_ride(self, ride: Ride) -> None:
        if ride not in self.requested_rides:
            raise ValueError
        ride_index = self.requested_rides.index(ride)
        self.rides.append(ride)
        self.requested_rides.pop(ride_index)

    def complete_ride(self, ride: Ride) -> None:
        if ride not in self.rides:
            raise ValueError
        ride_index = self.rides.index(ride)
        self.completed_rides.append(ride)
        self.rides.pop(ride_index)

    def rate_passenger(self, passenger: Passenger, rating: float) -> None:
        validate_type(rating, float)
        rating = f'Rating by {self.name}: {rating}. '
        passenger.ratings.append(rating)


from ride import Ride
from passenger import Passenger