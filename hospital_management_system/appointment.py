from utils.validators import String


class Appointment:
    name = String()

    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name
