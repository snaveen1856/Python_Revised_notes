l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = (sum(item) for item in zip(l1, l2))
print(type(l3), l3)

l4 = [sum(item) for item in zip(l1, l2)]
print(type(l4), l4)

string = 'this is a test string'
rev_str = ''
# l = string.split(' ')
# print(l)
for i in string.split(' ')[::-1]:
    rev_str += i
    rev_str += ' '
print(rev_str)
rev = ' '.join(string.split(' ')[::-1])
print(rev)
s = 'http://192.168.10.1/abfgj/iohknf'
list_1 = s.split('/')
print(list_1[2])

string_ = 'This is a String That is Good'
print(' '.join(string_.lower().split()[::-1]))



