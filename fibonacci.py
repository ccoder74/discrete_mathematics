"""
fibonacci.py:
    calculates and prints until nth fibonacci number
"""


def fib(n):
    if n in cache:  # Base case
        return cache[n]

    # Compute and ache the Fibonacci number
    cache[n] = fib(n - 1) + fib(n - 2)  # Recursive case

    return cache[n]


if __name__ == "__main__":
    cache = {0: 0, 1: 1}

    fib_num = int(input('\nEnter a positive integer: '))

    print(f'\nfibonacci of {fib_num}:')

    for num in range(fib_num):
        print(f'{fib(num)} ', end='')

    print('\n')
