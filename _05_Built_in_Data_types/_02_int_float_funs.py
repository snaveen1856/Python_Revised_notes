"""
'int()' is a built-in function,it accept float,string,bool and returns integer object.
where 'str' objects contains only digits that can be converted into 'int' object.
we can not convert complex object into integer object.

'float()' is a built-in function,it accept int,string,bool objects and returns float object.
where 'str' objects contains only digits that can be converted into 'int' object.
we can't convert the complex object into float object.

'str()' is a built-in function,it accept float,int,bool,complex and returns string object.
where string is immutable object we can not change once assigned.If we convert in str we can
not loss data.

'complex()' is a built-in function,it accept float,int,bool,str and returns complex object.
where 'str' objects contains only digits that can be converted into 'int' object.

'bool()' is a built-in function,it accept float,int,complex,str and returns bool object.
if a string object is empty or other than number (negative) also it will return a False,
otherwise True. Numerically it is True is '1' and False is '0'.

"""
a = 18.56
b = '1213'
c = True
d = 18 + 56j
x = int(a)
y = int(b)
z = int(c)
# s=int(d)
print('Type of a:', type(a))
print('Type of b:', type(b))
print('Type of c:', type(c))
print('Type of d:', type(d))
print('Type of x:', x, type(x))
print('Type of y:', y, type(y))
print('Type of z:', z, type(z))
# print('Type of s:',type(s))
''' ERROR:
   s=int(d)
TypeError: can't convert complex to int
'''
'''----------------------------------------------------------------------------'''
print('-' * 50)
a = 1856
b = '1213'
c = True
d = 18 + 56j
x = float(a)
y = float(b)
z = float(c)
# s=float(d)
print('Type of a:', type(a))
print('Type of b:', type(b))
print('Type of c:', type(c))
print('Type of d:', type(d))
print('Type of x:', x, type(x))
print('Type of y:', y, type(y))
print('Type of z:', z, type(z))
# print('Type of s:',type(s))
''' ERROR:
   s=float(d)
TypeError: can't convert complex to float
'''
'''----------------------------------------------------------------------------'''
print('-' * 50)
a = 18.56
b = 1213
c = True
d = 18 + 56j
x = str(a)
y = str(b)
z = str(c)
# s=str(d)
print('Type of a:', type(a))
print('Type of b:', type(b))
print('Type of c:', type(c))
print('Type of d:', type(d))
print('Type of x:', x, type(x))
print('Type of y:', y, type(y))
print('Type of z:', z, type(z))
# print('Type of s:',type(s))
''' ERROR:
   s=str(d)
TypeError: can't convert complex to str
'''
'''----------------------------------------------------------------------------'''
print('-' * 50)
a = 18.56
b = 1213
c = True
d = '18 + 56j'
x = complex(a)
y = complex(b)
z = complex(c)
# s=complex(d)
print('Type of a:', type(a))
print('Type of b:', type(b))
print('Type of c:', type(c))
print('Type of d:', type(d))
print('Type of x:', x, type(x))
print('Type of y:', y, type(y))
print('Type of z:', z, type(z))
# print('Type of s:',s,type(s))
'''ERROR:    s=complex(d)
ValueError: complex() arg is a malformed string
'''

'''----------------------------------------------------------------------------'''
print('-' * 50)
a = 18.56
b = 1213
c = 0
d = '18 + 56j'
e = ''
f = -5
x = bool(a)
y = bool(b)
z = bool(c)
s = bool(d)
n = bool(e)
k = bool(f)
print('Type of a:', type(a))
print('Type of b:', type(b))
print('Type of c:', type(c))
print('Type of d:', type(d))
print('Type of x:', x, type(x))
print('Type of y:', y, type(y))
print('Type of z:', z, type(z))
print('Type of s:', s, type(s))
print('Type of e:', e, type(e))
print('Type of f:', f, type(f))
print('Type of n:', n, type(n))
print('Type of k:', k, type(k))
