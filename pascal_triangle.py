"""
pascal_triangle.py:
    Print n levels of Pascal's Triangle
    User input: int(n)
"""

import math as m
import sympy as s

s.init_printing(pretty_print=True)

if __name__ == "__main__":
    row = int(input('Please enter row number (n >= 0): '))

    for i in range(row + 1):
        for j in range((row + 1) - i + 1):
            # Leaving spaces on the left side.
            print(end=" ")

        for j in range(i + 1):
            # nCr formula ====> nCr = n! / ((n - r)! * r!)
            print(m.factorial(i) //
                  (m.factorial(j) *
                   m.factorial(i - j)), end='')

        # for printing a new line
        print()

    print()

    n = s.Symbol('n')

    expr = 11**n

    s.pprint(expr)
    n = row
    print(f'\nn = {n}\n')
s.pprint(11**n)
