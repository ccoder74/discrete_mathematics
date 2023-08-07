"""
ordering.py:
    The number of orderings of n elements of which p elemnts are equal
    and the remaining elements are different is:

    N(orderings) = n! / p!
"""

from collections import Counter

import math as m

if __name__ == "__main__":
    mystring = input('Enter string: ').lower()
    mylist = list(mystring)

    mydict = dict((Counter(mylist)))

    p = []
    for value in mydict.values():
        if value > 1:
            p.append(value)

    divider = 1

    for faculty in p:
        divider *= m.factorial(int(faculty))

    print(f'N({mystring}) = {int(m.factorial(len(mylist)) / divider)}')
