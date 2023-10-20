"""
benet.py:
    calculates nth fibonacci number by direct formula of Binet
"""
import math as m

def binet(n):
    u = int(((1 + m.sqrt(5))**n - (1 - m.sqrt(5))**n) / (2**n * m.sqrt(5)))

    return u


if __name__ == "__main__":
    fib_num = int(input('\nEnter a positive integer: '))

    print(f'\nfibonacci of {fib_num}:')

    for num in range(fib_num):
        print(f'{binet(num)} ', end='')

    print('\n')
