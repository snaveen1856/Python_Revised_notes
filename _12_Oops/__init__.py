# Python code for type() with a name,
# bases and dict parameter

o1 = type('X', (object,), dict(a='Foo', b=12))

print(type(o1))
print(vars(o1))
print(o1.b)


class test:
    a = 'Foo'


b = 12

o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))
print(vars(o2))
