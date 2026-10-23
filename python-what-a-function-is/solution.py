def is_even(n: int) -> bool:
    return True if n % 2 == 0 else False


def greet_formal(name: str, title: str) -> str:
    return f'Good day, {title} {name}.'


def apply_twice(func, value):
    result = func(value)

    return func(result)
