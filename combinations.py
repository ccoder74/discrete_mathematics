"""
combinations.py:

    Choose k elements out of a set of n elements
    --------------------------------------------

    Combination:
    --------------------------------------------
    *) Unordered - No recurrence

       N(combinations) = (N over K)

                       = n! / (k! * (n - k)!)

    *) Unordered - Recurrence

       N(Recurrence Combinations) = ((n - 1 + k over k)
       1) n = n - 1 + k
       2) n! / (k! * (n - k)!)

"""

import math as m

if __name__ == "__main__":
    n = int(input(f'Enter number of elements (n): '))
    k = int(input(f'Enter number of elements (k): '))

    print(f'N(combinations) = {n}C{k} = {m.comb(n, k)}')
    print(f'N(Recurrent combinations) = {(n - 1) + k}C{k} = ', end='')
    print(f'{m.comb((n - 1) + k, n)}\n')
