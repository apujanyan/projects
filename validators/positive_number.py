from .validator import Validator


class Integer(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError(f'Expected {value} to be an int!')
        if value <= 0:
            raise ValueError('Passed value cannot be negative!')


class Number(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value} to be an int or float!')
        if value <= 0:
            raise ValueError('Passed value cannot be negative!')
