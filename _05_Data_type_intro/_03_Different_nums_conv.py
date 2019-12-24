""" Default number system is decimal number system.So, it convert any number system to decimal.
'0b' prefix numbers are 'Binary number'
'0o' prefix numbers are 'Octal-decimal number'
'0x' prefix numbers are 'Hexa-decimal number'
"""
a = 0b10101001
b = 0x1589acf
c = 0O75642
x = int(a)
y = int(b)
z = int(c)
print(a, type(a))
print(b, type(b))
print(c, type(c))
print('----------------------------------')
print(x, type(x))
print(y, type(y))
print(z, type(z))
print('------------------------------------')
s = bin(1856)
n = bin(0o75652)
k = bin(0x48569abf)
print(s)
print(n)
print(k)
print('------------------------------------')
j = oct(1213)
l = oct(0b10101001)
i = oct(0x4859621abf)
print(j)
print(l)
print(i)
print('------------------------------------')
m = hex(0b10100011)
p = hex(0o57461)
q = hex(1856)
print(m)
print(p)
print(q)
