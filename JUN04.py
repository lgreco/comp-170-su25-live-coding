# JUN 04 live coding

def f(x):
    return x*x

def h(x):
    return x*x-3

def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True 
    else:
        return False

def is_even_compact(n: int) -> bool:
    return (n % 2) == 0

def is_odd_compact(n: int) -> bool:
    return not is_even_compact(n)
    # return (n % 2) == 1
    


import datetime

def show_date():
    print(f"today is {datetime.date.today()}")


def tell_me_if_even(n: int):
    if n%2 == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")

def tell_parity(n: int):
    # We get special dispensation to allow printing this time.
    ODD = "odd"
    EVEN = "even"
    if n%2 == 0:
        parity = EVEN
    else: 
        parity = ODD
    print(f"Number {n} is {parity}")

def tell_parity_compact(n: int):    
    ODD = "odd"
    EVEN = "even"
    # Ternary operator -- simple if statement in a single line
    parity = "even" if n%2==0 else "odd"
    print(f"The number {n} is {parity}")


def print_first_numbers_upto(n: int):
    for i in range(n):
        print(i, end = " ")

print_first_numbers_upto(10)