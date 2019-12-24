string = input('Enter a string:')
l = string.split(' ')
# print(l)
reverse_l = []
res = ''
for i in l:
    rev_str = i[::-1]
    reverse_l.append(rev_str)
# print(reverse_l)
space = ' '
for i in reverse_l:
    res += i + space
print(res)