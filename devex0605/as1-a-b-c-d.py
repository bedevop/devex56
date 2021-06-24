# AS-1-A-B

# A
first = 7
second = 44.3
print("Result of {0} added {1} is"
      .format(first, second), first + second)
print("Result of {0} multiplied by {1} is"
      .format(first, second), first * second)
print("Result of {1} divided by {0} is"
      .format(first, second), second / first)

# B
a = 8
a = 17
a = 9  # final assignment to a
b = 6
c = a + b
b = c + a
b = 8  # final assignment to b
print("End values : a {0} b {1} c {2}".format(a, b, c))

# C
name = "john"
name = 'john'
print("Generally, have similar use except when quoting" + '"' + "double or single '" + "quotes")

my_number = 5 + 5
# print("Result is :" + my_number)
print("Result is : %d " % my_number,
      "Note : plus is for concatenation that expected a string when int was provided")

# D
x = 5
y = 2.36
print(x + int(y))
print("Prints result is 7, float is casted to int")

# *
a = 8
b = "123"
print(a + int(b))

