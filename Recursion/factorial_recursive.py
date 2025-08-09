def recursive_number_factorial(n):
    if n == 1:
        return 1
    return n * recursive_number_factorial(n - 1)