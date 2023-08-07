"""
sets.py:
    A set is a mutable, unordered group of elements, where the elements
    themselves are immutable.

    Intersection (V cap W)
    ----------------------
    Common elements of sets V and W.
    V cap W = {x|x in V AND x in W}

    Disjoint
    --------
    Sets V and W have no elements in common, i.e. an empty set.
    V cap W = {x|x NOT in V AND x NOT in W}

    Union (V cup W)
    ---------------
    Elements of V, elements of W or elements of both V and W.
    V cup W = {x|x in V OR x in W}

    Difference (V \\ W)
    ------------------
    Elements of V but not the elements of W.
    V \\ W = {x|x in V AND x NOT in W}

    Product (V x W)
    ---------------
    V x W = {(x, y)|x in V AND y in W}

    Subset (V subset(eq) W)
    -----------------------
    Every element of V is also an element of W.
    1) V = W (V subseteq W)
    2) V < W (V proper subset W)

    Superset (V superset(eq) W)
    ---------------------------
    Every element of W is also an element of V plus the elements of V
    that are not element of W.
    1) V = W (V supseteq V)
    2) V > W (V proper supset W)

    Occurence in an experiment
    --------------------------
    An occurence O in an experiment with outcome set U is a subset of U.
    #(O) is the number of elements of O.

    Product-rule
    ------------
    An experiment involving
        - experiment 1 with n_1 outcomes and
        - experiment 2 with n_2 outcomes and
        - experiment 3 with n_3 outcomes and ...
    has n_1 * n_2 * n_3 * ... outcomes

    Summation-rule
    --------------
    Summation of sets A and B involves first adding the number of elements of
    A and B and subtract the number of elements of the intersection of sets
    A and B.

    Non-disjoint sets:
    #(A cup B) = #(A) + #(B) - #(A cap B)

    Disjoint sets:
    #(A cup B) = #(A) + #(B)
"""

if __name__ == "__main__":
    print()
    V = set(input('Enter the elements of set V: '))
    W = set(input('Enter the elements of set W: '))

    print()
    print(f'V = {V}    #(V) = {len(V)}')
    print(f'W = {W}    #(W) = {len(W)}')

    print()
    if V.isdisjoint(W):
        print('V and W are disjoint.')
        print(f'#(V) + #(W): {len(V) + len(W)}')
    else:
        print(f'V intersect W = {V.intersection(W)}.')
        print(f'#(V) + #(W) - #(V intersect W) = ', end='')
        print(f'{len(V) + len(W) - len(V.intersection(W))}')

    if V.issubset(W):
        print('V subset W, and', end=' ')
        if V == W:
            print('V = W.')
        else:
            print('V proper subset W.')
    elif W.issubset(V):
        print('W subset V, and', end=' ')
        if W == V:
            print('W = V.')
        else:
            print('W proper subset V.')

    if V.issuperset(W):
        print('V superset W, and ', end='')
        if V == W:
            print('V = W.')
        else:
            print('V proper superset W.')
    elif W.issuperset(V):
        print('W superset V, and ', end='')
        if W == V:
            print('W = V.')
        else:
            print('W proper superset V.')

    if not V.isdisjoint(W):
        if len(V) > len(W):
            print(f'V\\W = {V.difference(W)}')
        if len(W) > len(V):
            print(f'W\\V = {W.difference(V)}')

    print(f'\nV union W = {V.union(W)}\n')
