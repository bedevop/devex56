# AS2, Part II, Igal.S
import phonenumbers
from phonenumbers import NumberParseException

# F
"""
print('F.')
phone_number = input('Input Phone Number : ')
try:
    phone_number_parsed = phonenumbers.parse(phone_number)
    valid = 'is valid' if phonenumbers.is_valid_number(phone_number_parsed) else 'not valid'
except NumberParseException:
    valid = '(probably not a number)'
print( 'Phone number :', phone_number, valid)
"""

# F
print('F.')
print('phone number', input('Input pn : '))

# G
print('G.')


def printHello():
    print('hello')


def calculate():
    print(5 + 3.2)


printHello()
calculate()

# H
print('H.')


def print_my_name(name):
    print(name)


def divide_number_by_two(number):
    print(number / 2)


print_my_name('Igal.S')
divide_number_by_two(3)

# I
print('I.')


def sum_two_numbers(x, y):
    return x + y


def concat_two_strings_ws(s1, s2):
    return s1 + ' ' + s2


print(sum_two_numbers(7, 7))
print(concat_two_strings_ws('ssstr', 'ssssssssstr'))
