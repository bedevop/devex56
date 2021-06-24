import time


def read_from_file(i_f, mod):
    try:
        f = open(i_f, mod)
    except BaseException as e:
        print(e)


read_from_file(input('Read from file : '),input('Mod : '))


'''
mf = open('read_from_this_file.txt')
for line in mf.readlines():
    if 'xxx' in line:
        print(line, end='')
    else:
        continue

# write to file
mf = open('12-read_from_this_file_z.txt','a')
mf.write(str(time.time()))
mf.close()


# write names to file
def write_name_to_file(f):
    h = open(f, 'a').write(input('Input name') + '\n')


names_file = '12-names_file'
for i in range(0, 3):
    write_name_to_file(names_file)
'''


