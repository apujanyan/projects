from .validator import Validator
from datetime import datetime


class DateTime(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, datetime):
            raise TypeError(f'Expected {value} to be a datetime type!')
