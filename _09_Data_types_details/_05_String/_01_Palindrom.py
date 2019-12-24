"""Print palindrom or not Using slice operator and l.reverse function"""

s = input("Enter a word:")
rev_s = s[::-1]
if rev_s == s:
    print('It is a panlindrom:')
else:
    print('Its not a panlindrom:')

print('-' * 50)
'''Another logic code for palindrom '''

l = list(s)
print(l)
l.reverse()
rs = ''
for i in l:
    rs += i
print('Reverse the string:', rs)
if rs == s:
    print('It is a panlindrom!')
else:
    print('Its not a panlindrom!')

print('Encode of String:', s.encode())
print('Extandable of String:', s.expandtabs(), ':', s)
print('Encode of String:', s.format())
