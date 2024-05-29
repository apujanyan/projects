from utils.validators import Number, Integer, String


class Room:
    number = Integer()
    price = Number()
    amenity = String()

    def __init__(self, number: int, price: float, amenity: str) -> None:
        self.number = number
        self.price = price
        self.amenity = amenity
        self.is_available = True

    def get_description(self) -> None:
        print(f'Room: Number {self.number}: Price {self.price}. ')


class Deluxe(Room):
    def get_description(self) -> None:
        print(f'Deluxe room: Number {self.number}: Price {self.price}. ')


class Economy(Room):
    def get_description(self) -> None:
        print(f'Economy room: Number {self.number}: Price {self.price}. ')
