from .validator import Validator


class String(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f'Expected {value} to be a str!')
        if value == '':
            raise ValueError('Passed value cannot be an empty string!')
