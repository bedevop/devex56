def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


# Write a function that takes in a numerical value, and returns
#  the word corresponding to that number.
# The program will handle numbers: 0 - 4, for other numbers it will
# return that the input is incorrect.

def get_numeric(number):
    numbers = ["zero", "one", "two", "three", "four"]
    if number < len(numbers):
        return numbers[number]
    else:
        return "not supported"


a = 6


def my_function(x):
    print(x * a)


def my_function1(x, a):
    print(x * a)


def my_function2(x):
    a = 6
    print(x * a)

