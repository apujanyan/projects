from __future__ import annotations
from utils.validators import String, Number


class Ride:
    destination = String()
    fare = Number()

    def __init__(
            self,
            driver: Driver,
            passenger: Passenger,
            destination: str,
            fare: float
    ) -> None:
        self.driver = driver
        self.passenger = passenger
        self.destination = destination
        self.fare = fare

    def __repr__(self) -> str:
        return f'Ride for {self.passenger.name}, driver is {self.driver.name}. '


from driver import Driver
from passenger import Passenger
