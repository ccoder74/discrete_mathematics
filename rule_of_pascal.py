"""
rule_of_pascal.py:
    In Pascal's triangle, each number is the sum of the two numbers diagonally
    above it. This number is the binomial coefficient.

    n! / (k - 1)!(n - k + 1)! + n! / k!(n - k)! = (n + 1)! / k!(n + 1 - k)!
"""

import math as m

if __name__ == "__main__":
    print('Calculation binomial coefficient.')
    n = int(input("Please enter n: "))
    k = int(input("Please enter k: "))

    print(f'The sum of row {n} column {k} is ', end='')
    print(f'{m.comb(n, k - 1)} + {m.comb(n, k)} = {m.comb(n + 1, k)}')
