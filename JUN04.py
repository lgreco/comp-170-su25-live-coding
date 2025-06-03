# JUN 04 live coding

def f(x: int) -> int:
    """Squares a given number.
    
    Input
    -----
    x : int
      number to square 
    
    Returns
    -------
    int
      the number squared
    """
    return x * x

# Simple print
print(f(5))

# Fancy print
x = 6
print(f"\nThe square of {x} is {f(x)}\n")
