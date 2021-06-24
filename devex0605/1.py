print("Hello")

person1 = ["Aviel", "Buskila", 31, True]
person2 = {"fname": "Aviel", "lname": "Buskila", "age": 31, "w": True}

print(person2.keys())

x = 4
if x == 4:
    print("x is eq4")

a = 4 + 3
b = 4 + 2.0
print(a)
print(type(b))
c = 4 + 3
d = "aviel" * 4
print(d)
e = "aviel" + "moshe"
print(e)

nn = f" {e,d,c}"
print(nn)
print(type(nn))

# string format
age = 31
print("your age is : " + str(31))
print(f"your age is : {age}")
print("your name is : %s %s" % ("zzzz","yyyy"))

j = 4/3
print(j)


