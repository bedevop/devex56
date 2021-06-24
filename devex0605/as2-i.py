# AS-2, Part I, Igal.S
import random


# * Dictionary validation
def valid(dic):
    struct = {"name": str, "age": int, "Hobbies": list}
    for k, v in dic.items():
        if k not in struct.keys():
            print('not in list key ' + k)
            continue
        if type(v) != struct[k]:
            print(k + ' Expected ' + str(struct[k]) + ' got ' + str(type(v)))


# A
print ('A.')
# x, y = input(), input()
x = 12
y = 2
if x > y:
    print('BIG')
elif x < y:
    print('small')

# B
print ('B.')
for it in range(5):
    print('it', it)

# C
print ('C.')
vv = random.randrange(1, 5)
if vv == 1:
    print('summer')
elif vv == 2:
    print('winter')
elif vv == 3:
    print('fall')
elif vv == 4:
    print('spring')

# D
print ('D.')
c = 1
while c < 11:
    print(c)
    c = c + 1

# E
print ('E.')
z = 0
sum_keys = ("Age", "App")
zzz = {"Age": 40, "First Letter": "S", "CC": "nis", "Fly": False, "App": 40}
for k, zz in zzz.items():
    print(zz)
    if k in sum_keys:
        z = z + zz

print(zzz)
print("Sum of", sum_keys, "is", z)
