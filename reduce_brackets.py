"""
reduce_brackets.py:
    Expand (a + b)^n
    User input: (int)n
    n = 0 -> 1
    n = 1 -> a + b
    n = 2 -> a^2 + 2ab + b^2
    n = 3 -> a^3 + 3a^2b + 3ab^2 + b^3
    ...
"""

if __name__ == "__main__":
    import sympy as s

    a, b = s.symbols('a b')

    n = int(input('Please enter n (n >= 0): '))

    expr = (a + b) ** n
    expr_sim = s.simplify(expr)
    expr_exp = s.expand(expr_sim)

    s.pprint(expr_exp)
