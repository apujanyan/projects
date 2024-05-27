from utils.validators import Integer, String


class Patient:
    name = String()
    age = Integer()

    def __init__(
            self,
            name: str,
            age: int,
    ) -> None:
        self.name = name
        self.age = age
        self.medical_history = []