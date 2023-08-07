"""
seq_num.py:
    prints a sequence of numbers
"""

if __name__ == "__main__":
    start_val = float(input('Enter start value: '))
    mult_val = float(input('Enter multiplication value: '))
    add_val = float(input('Enter add value: '))
    num_terms = int(input('Enter number of terms: '))

    u0 = start_val
    print()

    for num in range(num_terms):
        print(f'u{num} = {u0}')
        u0 *= mult_val
        u0 += add_val

    print()
