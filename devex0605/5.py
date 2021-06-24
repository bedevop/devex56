names = ['ddd', '444', 'fff']
print(list(range(2, 5)))
print(list(range(10, -5, -3)))
print(list(range(10)))

for i in range(4):
    print('h')

for i in range(len(names)):
    print("hi", names[i])

print(range(10))

for n in names:
    print("hi %s" % n)

a = 0
while a < 5:
    print('still a %d' %a)
    a += 1

for n in names:
    if n == '444' and print('nah'):
        continue
    print("hi %s" % n)

a = 0
while a < 5:
    print('still a %d' %a)
    a += 1
else:
    print('setu')

for n in names:
    if n == '444' and print('nah'):
        continue
    print("hi %s" % n)
else:
    print('se tu')

for n in names:
    if n == '444':
        continue
    print("hi %s" % n)
else:
    print('se-tu')

for n in names:
    if n == '444':
        break
    print("hi %s" % n)
else:
    print('se-tu')

for z in range(100):
    if z % 7:
        print('#',z)
    else:
        print('boom')

[print(i) for i in range(1, 101) if i % 7]

[print('boom') if not x % 7 or '7' in str(x) else print(x) for x in range(1, 101)]
