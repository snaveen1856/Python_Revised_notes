# print() styles

name = input('Enter name:')
age = int(input('Enter age:'))
# python 2 style
# print('Hello %s you are %d years old' %(name,age))
# python 3 style
# print(f"Hello {name} you are {age} years old")
# print("Hello {:10s} you are {:5d} years old".format(name,age))
print("Hello {} you are {}  years old".format(age, name, age))
print("Hello {n:10s} {n:10s} you are {} years old".format(n=name, a=age))
