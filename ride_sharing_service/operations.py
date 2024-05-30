from abc import ABC, abstractmethod


class PassengerOperations(ABC):
    @abstractmethod
    def request_ride(self, driver, destination, fare):
        pass


class DriverOperations(ABC):
    @abstractmethod
    def accept_ride(self, ride):
        pass

    @abstractmethod
    def complete_ride(self, ride):
        pass
