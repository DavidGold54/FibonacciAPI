import re


def validate_positive_integer(value: str) -> int:
    pattern = r'^[1-9]\d*$'
    if not re.match(pattern, value):
        raise ValueError("Input value must be a positive integer.")
    return int(value)