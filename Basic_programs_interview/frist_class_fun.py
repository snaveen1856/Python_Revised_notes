def add(abc):
    return abc + 2


def sub(xyz):
    return xyz - 2


def firstClass(fun_name, val):
    if fun_name == add:
        res = add(val)
    else:
        res = sub(val)
    return res + 1


a = firstClass(add, 1)
print(a)
s = firstClass(sub, 4)
print(s)
x = firstClass
a = x(add, 1)
print(str(x(add, 1)) + '2')
