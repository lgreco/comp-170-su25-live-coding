def is_odd(n: int) -> bool:
    """Determines if a number is odd or even"""
    if n % 2 == 0:
        result = False
    else:
        result = True
    return result


def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd_optimized(n: int) -> bool:
    if n % 2 == 0:
        return False
    return True


def is_even_optimized(n: int) -> bool:
    result = False
    if n % 2 == 0:
        result = True
    return result


def is_odd_final(n: int) -> bool:
    return n % 2 == 1


def is_even_final(n: int) -> bool:
    return not is_odd_final(n)


import math # needed for square root function

def solve_quadratic(a, b, c):
    """Solves a*x*x + b*x + c = 0 for real-valued x."""
    x1 = None
    x2 = None
    if b * b - 4 * a * c > 0:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    elif b * b - 4 * a * c == 0:
        x1 = -b / (2 * a)
        x2 = x1
    return x1, x2

