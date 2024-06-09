import re


def validate_positive_integer(value: int) -> int:
    # 正の整数値のみを許容する正規表現
    pattern = r'^[1-9]\d*$'
    
    if not re.match(pattern, str(value)):
        raise ValueError("Input value must be a positive integer.")
    
    if value > 20577:
        raise ValueError("Input value is too big.")

    return value