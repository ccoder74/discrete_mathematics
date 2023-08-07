"""
binomium_python.py:

    Newton's binomium:
    (a + b)^n = Sigma(k = 0 ... k = n) (n! / k! * (n - k)!) * a^(n - k) * b^k

        - user input: binomial coefficients n and k
        - calculate Newton's binomium with n choose k
"""

import sympy as s

if __name__ == "__main__":
    s.init_printing(use_latex='mathjax')

    print('\nReduce and expand (a + b)^n or (a-b)^n.')

    expr = input("Enter binomial expression using Python operators: ")

    simple_expr = s.simplify(expr)
    expand_expr = s.expand(expr)

    s.pprint(simple_expr)
    print()
    s.pprint(expand_expr)
