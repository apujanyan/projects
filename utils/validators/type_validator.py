def validate_type(value, expected_type):
    if not isinstance(value, expected_type):
        raise TypeError(f'Expected {value} to be '
                        f'{expected_type.__name__} type!')