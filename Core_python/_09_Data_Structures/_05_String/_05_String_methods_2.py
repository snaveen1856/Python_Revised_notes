""" ------Immutable,Replace,Change case and checking Start & Ending of String------ """
print('---------Immutable of String----------')
str1 = 'abcd'
print(str1, str1[0], str1[3])
'''
str1[0]='x'
ERROR:
   str[0]='x'
TypeError: 'str' object does not support item assignment  '''
a = 'Naveen'
b = 'Chinni'
print('Object reference address of a:', a, id(a))
print('Object reference address of b:', b, id(b))
a = b  # Here not change string object a to b,just assign 'a' grabage collection
print('After Assigning a=b Object reference address of a:', id(a))
print('After Assigning a=b Object reference address of b', id(b))
print('---------Replacing of String----------')
s = 'That is a Beautiful girl'
s1 = 'That'
s2 = 'Sindhu'
print('Old String:', s)
n = s.replace(s1, s2)
print('After changing string:', n)
print('---------Splitting and Joining of String----------')
k = 'one,two,three,four,five,six,seven,eight,nine,ten'
l = k.split(',')
print(l)
for a in l:
    print(a)
m = 'Hi! Chinni How are you doing I am fine here'
p = m.split(' ')  # Default seperator is space it will take and do operation
print(p)
sep = ':'
q = sep.join(p)
r = '-'.join(l)
print('After joining:', q)
print('After joining:', r)
print('-------------Changing Case of String--------------')
g = 'python is the future'
j = g.upper()
print('Entered string: ', g)
print('After upper Casing: ', j)
h = j.lower()
print('After lower Casing: ', h)
t = 'surya ganga restaurant and resorts'
x = t.title()
print("After change to title of string:", x)
c = x.swapcase()
print("After Swaping the characters of string:", c)
print('-------------Checking Starting and Ending of String--------------')
string1 = 'This is a Python language and it is a future'
print(string1)
print(string1.startswith('Th'))
print(string1.startswith('th'))
print('---endswith() method---')
print(string1.endswith('re'))
print(string1.endswith('tURE'))
