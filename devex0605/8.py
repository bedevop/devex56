def how_many(li):
    return len(li)


def valid(dic):
    struct = {"name": str, "age": int, "Hobbies": list}
    for k, v in dic.items():
        if k not in struct.keys():
            print('not in list key ' + k)
            continue
        if type(v) != struct[k]:
            print(k + ' Expected ' + str(struct[k]) + ' got ' + str(type(v)))


a_list = [4, 'f', 'hh', 'ggg']
print(how_many(a_list), '...')

a_dic = {"name": 'ff', "age": 77, "Hobbies": ['bla', 'foo', 'BAR']}
valid(a_dic)
valid({"name": 0, "age": 77, "hob": ['bla', 'foo', 'BAR']})
