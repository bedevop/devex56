# AS2, Part III, Igal.S

# K
print('K.')


def print_pyramid(size, symbol):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(symbol, end='')
        print('\r')


print_pyramid(7, '#')

# L
print('L.')


def print_x_shape(size, symbol, space=' ', mid='@'):
    if size < 3:
        size = 3
    if not size & 1:
        size += 1
    for i in range(0, size):
        if i < int(size / 2):
            line = space * i + symbol
            for j in range(0, size - 2 - i * 2):
                line += space
            line += symbol + space * i
        elif i == int(size / 2):
            line = i * space + mid + space * i
        else:
            line = space * (size - i - 1) + symbol
            for j in range(0, i * 2 - size):
                line += space
            line += symbol + space * (size - i - 1)
        print(line)


print_x_shape(77, 'X', '_')

# M
print('M.')


def get_number_input():
    return input('Input number :')


def compute_digits(user_input):
    digit_sum = 0
    for i in user_input:
        try:
            digit_sum += int(i)
        except ValueError:
            return 'Value Error'
    return digit_sum


print(compute_digits(get_number_input()))
