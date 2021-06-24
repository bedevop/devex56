def sq(n):
    r = n * n
    return r


def mul_and_sum(a, b):
    mul = a * b
    sum1 = a + b
    return mul, sum1


def mul_and_sum1(a, b):
    mul = a * b
    sum1 = a + b
    return {"m": mul, "s": sum1}


a = sq(20)
print(a)

result = mul_and_sum(5, 7)
print(type(result))
print(result)
result = mul_and_sum1(5, 7)
print(result)
print(result['s'])

me = input()
print('me' + me)

