from add_numbers import add_numbers


def get_numbers_and_add():
    a = int(input('Input number: '))
    b = int(input('Enter second number: '))
    return add_numbers(a, b)


get_numbers_and_add()
