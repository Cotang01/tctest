

def add_numbers(n1: int | float, n2: int | float) -> int | float:
    n1_float_len = 0
    n2_float_len = 0
    if isinstance(n1, float):
        n1_float_len = len(str(n1).split('.')[-1])
    if isinstance(n2, float):
        n2_float_len = len(str(n2).split('.')[-1])
    return round(n1 + n2, max(n1_float_len, n2_float_len))
