"""
meltinomium.py:
    User Input: polynomial
    Returns: possible sequences of multinomial coefficients
"""

from math import comb, factorial
from sympy import Poly, expand, init_printing, pprint, simplify, symbols
from sympy.abc import a, b, c

if __name__ == "__main__":
    init_printing(use_latex='mathjax')

    print('\nReturns multinomial coefficients of polynomial.')

    expr = input("Enter polynomial using (a, b, c): ")

    print('\nPolynomial:\n')
    pprint(simplify(expr))
    print('\nTerms:\n')
    print(Poly(eval(expr), a, b, c).monoms())
    print(f\n'N(terms) = ((3 - 1 + 6) over 6) = (8 over 6) = {comb(3-1+6,6)}')
    print('\nExpansion polynomial:\n')
    pprint(expand(expr))
    print('\nCalculate coefficient of term.\n')
    powers = [int(x) for x in input('Enter powers of a, b and c: ')]
    print('\nCoefficient of term:\n')

    sum_powers = 0

    for num in powers:
        sum_powers += int(num)

    fac_n = factorial(sum_powers)
    fac_k1 = int(factorial(powers[0]))
    fac_k2 = int(factorial(powers[1]))
    fac_k3 = int(factorial(powers[2]))

    recur_comb = int(fac_n / (fac_k1 * fac_k2 * fac_k3))
    coefficient = recur_comb * 2**powers[0] * (-3)**powers[1] * 4**powers[2]

    print(f'Coefficient is {coefficient}.\n')
