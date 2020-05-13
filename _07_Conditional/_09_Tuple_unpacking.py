""" Multiple Assigning and unpacking of tuple """

a, b = (18, 56)
print("a=", a, '\n', "b=", b)
c, _ = (12, 13)
print("c=", c, "_=", _)
d, e, *f = (14, 13, 18, 56, 20, 45, 46)
print("d=", d)
print("e=", e)
print("f=", f)
a, b, c, *d, e = (12, 45, 89, 78, 46, 56, 23, 46, 9, 4, 6, 13, 72, 36, 42, 48, 49, 52, 57, 99)
print("a=", a, "\n", "b=", b, "\n", "c=", c, "\n", "d=", d, "\n", "e=", e)
