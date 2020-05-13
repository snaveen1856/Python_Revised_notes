"""Print palindrome or not Using slice operator and l.reverse function"""

s = input("Enter a word:")
rev_s = s[::-1]
print('Palindrome using in built Slicing method')
if rev_s == s:
    print('It is a palindrome:')
else:
    print('Its not a palindrome:')

print('-' * 50)
'''Another logic code for palindrome '''

# l = list(s)
# print(l)
# l.reverse()
rs = ''
for i in s:
    rs += i
print('Reverse the string using a loop concept:', rs)
if rs == s:
    print('It is a palindrome!')
else:
    print('Its not a palindrome!')

print('-' * 50)
print('Encode of String:', s.encode())
print('Extendable of String:', s.expandtabs(), ':', s)
print('Encode of String:', s.format())
print('-' * 50)
n = list(''.join(s.lower().split()))
print(n.reverse())
print('n value:', n, type(n))
