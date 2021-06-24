isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

if isTrue is False and a == 2:
    print("hello")

if strOne != "Two" or strThree == "Three":
    print("hey")

if not b == 2.5:
    print("b is not 2.5")

if a < 2 and b > 2.5:
    print("v")

if 1 <= b <= 100:
    print("b is between")

if print('z') and a == 2.6:
    print("h")
elif a == 2.4:
    print('nope')
else:
    print('p')

# list
nms = ['aaa', 'bbb']
my_name = 'jjj'

if print('checking name..') and my_name in nms:
    print("name %s found" % my_name)
else:
    print("%s not found" % my_name)

print(1 == 1)

c = [1, 2, 3]
d = [1, 2, 3]

e = c
f = 5
g = 5

print(c == d)
print(c is d)
print(e == c)
print(f == g)
print(f is g)

h = [1, 2, 3]
i = []
if h:
    print('h has el')
if i:
    print('i has el')

if len(h):
    print('len h %d' % len(h))

i = []
if len(i):
    print('Zero')

