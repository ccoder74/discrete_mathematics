"""
sigma.py:
    The sigma notation is used to briefly write down the sum of a number of
    numbers having a certain property.
"""


def sigma_sum(start, end, expression):
    return sum(expression(i) for i in range(start, end))


if __name__ == "__main__":
    print('Calculate Sigma (Sum).')
    k_lower = int(input('Enter lower value k: '))
    k_upper = int(input('Enter upper value k: '))
    lambda_expr = input('Enter formula to be summed using Python operators: ')

    print(sigma_sum(k_lower, k_upper + 1, lambda k: eval(lambda_expr)))
