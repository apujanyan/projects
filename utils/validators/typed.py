def typed(fn):
    def wrapper(*args, **kwargs):
        types = fn.__annotations__
        varnames = fn.__code__.co_varnames
        for arg_name, arg_value in zip(varnames, args):
            if arg_name in types:
                if not isinstance(arg_value, types[arg_name]):
                    raise TypeError(f'Expected {arg_value} to be '
                                    f'{types[arg_name].__name__} type!')
        for arg_name, arg_value in kwargs.items():
            if arg_name in types:
                if not isinstance(arg_value, types[arg_name]):
                    raise TypeError(f'Expected {arg_value} to be '
                                    f'{types[arg_name].__name__} type!')
        return fn(*args, **kwargs)
    return wrapper
