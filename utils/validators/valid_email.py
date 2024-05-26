import re
from .validator import Validator


class Email(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f'Expected {value} to be a str!')
        email_pattern = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        if not email_pattern.fullmatch(value):
            raise ValueError('Invalid email pattern!')
