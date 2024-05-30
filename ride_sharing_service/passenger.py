from __future__ import annotations
from operations import PassengerOperations
from utils.validators import String, Email, validate_type


class Passenger(PassengerOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.ratings = []

    def request_ride(
            self,
            driver: Driver,
            destination: str,
            fare: float
    ) -> Ride:
        ride = Ride(driver, self, destination, fare)
        driver.requested_rides.append(ride)
        return ride

    def rate_driver(self, driver: Driver, rating: float) -> None:
        validate_type(rating, float)
        rating = f'Rating by {self.name}, {rating}. '
        driver.ratings.append(rating)


from driver import Driver
from ride import Ride
