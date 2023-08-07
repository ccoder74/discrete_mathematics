"""
variations.py:
    Choose k elements out of a set of n elements
    --------------------------------------------

    Variation:
    --------------------------------------------
    *) Ordered - No recurrence

       N(variations) = nPk = n! / (n - k)!
       N(permutations) = n! (k = n)

    *) Ordered - Recurrence

       N(recurrent variations) = n^k
    --------------------------------------------
"""

import math as m

if __name__ == "__main__":
    n = int(input(f'\nEnter number of elements (n): '))
    k = int(input(f'Enter number of elements (k): '))

    print(f'\nN(Recurrence variations) = {n}^{k} = {n ** k}')
    print(f'N(Variations) = {n}P{k} = {m.perm(n, k)}')
    print(f'N(Permutations) = {n}P{n} = {n}! = {m.factorial(n)}')
