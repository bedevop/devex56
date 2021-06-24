# AS-3, Igal
# -*- coding: utf-8 -*-
import time


# 1, 2
print('# 1,2')
try:
    a = 1 / 0
except ZeroDivisionError as e:
    print('Division by zero', e.args)

# 3
print('# 3')
try:
    x = 1
finally:
    print('finally')

'''''
def func1():
    try:
        z = 'z'
        return 1
    finally:
        return (z, 2)


def func2():
    try:
        raise ValueError()
    except:
        return 1
    finally:
        return 3


print('f1', func1())
print('f2', func2())
'''''

# 4
print('# 4')
print('Python Logical Errors, Errors that occur at runtime (after passing the syntax test) are called exceptions or '
      'logical errors')

for loc in dir(locals()['__builtins__']):
    if 'Error' in loc:
        print(loc)

# 5
print('# 5')
print('Too broad exception clause')

# 6
print('# 6')
print(
    'IOError : Now the error like these, which are detected during the program execution are known as exceptions. '
    'Commonly, the IOError is raised when an input output operation like open () file, or a method or a simple print '
    'statement is failed due to IO reasons like “Disk full” or “File not found”')
print('Division by zero.')

# 7, 8, 9, 10
print('# 7, 8, 9, 10')

file_name = str(int(time.time())) + '_file.txt'
file_stream = open(file_name, "w+", encoding="utf-8")
print('File name: ' + file_name)

file_stream.writelines(['I\n', 'G\n', 'A\n', 'L\n'])
file_stream.seek(0)
print('Characters in file :', len(file_stream.read()))
file_stream.seek(0)
print(file_stream.read())
f_last_read = file_stream.tell()

str_ = 'יגאל'
print(str_)
str_e = str_.encode('utf8')
print(str_e)

file_stream.write(str_)
file_stream.seek(f_last_read)
print(file_stream.read())
file_stream.close()

file_name = str(int(time.time())) + '_b_file.txt'
file_stream = open(file_name, "wb+")
print('File name: ' + file_name)
str_b = 'אבגדהוזחטיכל'
str_c = 'abcdefghzzz'
file_stream.write(str_b.encode() + str_c.encode())
for _ in ('foo', 'bar', '-ששש-'):
    _ += '_\n'
    file_stream.write(_.encode())
file_stream.seek(0)
print(file_stream.read().decode())
file_stream.close()

