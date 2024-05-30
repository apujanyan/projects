from costumer import Costumer
from dealership import CarDealership
from salesman import Salesman
from cars import PetrolCar, ElectricCar


def main() -> None:
    dealership = CarDealership()

    bob = Costumer('Bob', 'bob@mail.com')
    jack = Salesman('Jack', 50)

    tesla = ElectricCar('Model X', 'Tesla', 50000)
    camry = PetrolCar('Camry', 'Toyota', 20000)

    jack.add_car(dealership, tesla)
    jack.add_car(dealership, camry)

    bob.purchase_car(dealership, tesla, jack,100000)


if __name__ == '__main__':
    main()
