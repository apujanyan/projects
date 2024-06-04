from .validator import Validator


class CustomValidator(Validator):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def validate(self, value) -> None:
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {value} to be '
                            f'{self.expected_type.__name__} type!')


class ArgsCustomValidator(Validator):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def validate(self, value) -> None:
        for val in value:
            if not isinstance(val, self.expected_type):
                raise TypeError(f'Expected {val} to be '
                                f'{self.expected_type.__name__} type!')
