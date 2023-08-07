"""
pow_exp_div.py:
    Calculation rule: a^p / a^q = a^(p-q)
    If q = p then a^p / a^p = a^(p-p) = a^0 = 1
"""

from sympy import *

if __name__ == "__main__":
    a = Symbol('a')
    p, q = symbols('p q')

    pprint(a**p / a**q, use_unicode=True)
    print()
    pprint(simplify(a**p / a**q), use_unicode=True)
