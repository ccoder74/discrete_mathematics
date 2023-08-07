"""
polygon.py:
    Calculates the number of diagonals of a regular polygon.
    A regular polygon is equiangular (all vertex angles are equal) and
    equilateral (all edges are of the same length).

    Formula of number of edges in a regular polygon:

    N = nC2 - 2 = (n(n-1)) / 2 - n = 0.5n^2 - 0.5n - n = 0.5n^2 - 1.5n
"""

import math as m

if __name__ == "__main__":
    polygon = {
        '3': 'triangle',
        '4': 'tetragon',
        '5': 'pentagon',
        '6': 'hexagon',
        '7': 'heptagon',
        '8': 'octagon',
        '9': 'nonagon',
        '10': 'decagon',
        '11': 'hendecagon',
        '12': 'dodecagon',
        '13': 'tridecagon',
        '14': 'tetradecagon',
        '15': 'pentadecagon',
        '16': 'hexadecagon',
        '17': 'heptadecagon',
        '18': 'octadecagon',
        '19': 'enneadecagon',
        '20': 'icosagon',
        '23': 'icositrigon',
        '24': 'icositetragon',
        '30': 'triacontagon'
    }

    not_in_polygon = True
    n = '0'

    while not_in_polygon:
        n = input('\nEnter the number of angles of the polygon: ')

        if n in polygon:
            not_in_polygon = False

    print(f'\nA {polygon[n]} has {int(n)} edges.')
    print(f'N(connecting line segments) = {int(n)}C2 = ', end='')
    print(f'{int(n)}! / (2!{int(n) - 2}!) = {m.comb(int(n),int(2))}')
    print(f'N(diagonals) = {m.comb(int(n), int(2))} - {int(n)} = ', end='')
    print(f'{m.comb(int(n), int(2)) - int(n)}')
    print(f'N(diagonals) = 0.5n^2 - 1.5n = 0.5 * {int(n)}^2 - 1.5 * ', end='')
    print(f'{int(n)} = {int(0.5 * int(n)**2 - 1.5 * int(n))}')
