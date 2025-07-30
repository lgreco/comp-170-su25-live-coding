def fibonacci(n):
    return n if (n==0 or n==1) else fibonacci(n-1)+fibonacci(n-2)

def fibonacci_iter(n):
    i = 2
    previous = 0
    previous_previous = 1
    while i < n:
        temp = previous + previous_previous
        previous_previous = previous
        previous = temp
        i += 1
    return previous


for i in range(1001):
    print(f"{i:3d}: {fibonacci_iter(i)}")

