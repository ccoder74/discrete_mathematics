"""
sum_geo_seq.py:
    For a geometric sequence (gm) u(n) with factor r holds:

    1) S(k = 0 to n) u(k) = (u(0) - u(n + 1)) / (1 - r)

    and also

    2) S(k = 0 to n) u(k) = u(0) * ((1 - r(n + 1)) / (1 - r))
"""

if __name__ == '__main__':
    k = 0
    n = int(input('Enter a value for n > 0: '))
    r = float(input('Enter a value for r: '))
    u0 = float(input('Enter a value for u0: '))

    print(f'\ngm: u(n) = {int(u0)} * {r}^n with initial term u(0).\n')

    # first formula S
    print(f'S(k = 0 to {n}) = {int(u0)} * {r}^k = ', end='')
    print(f'{u0 * ((1 - r ** (n + 1)) / (1 - r))}\n')

    k = int(input('Enter another value for k > 0: '))
    n = int(input('Enter another value for n > k: '))

    # second formula S
    print(f'\nS(k = {k} to {n}) = {int(u0)} * {r}^k = ', end='')
    print(f'{round((u0 * r ** k - u0 * r ** (n + 1)) / (1 - r))}\n')
