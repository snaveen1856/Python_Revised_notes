s = input('Enter a test string:')
print('Length of a string:', len(s))
print('-------------Indexing of string---------------')
i = input('Enter a character to know index:')
print('Index of a string:', s.index(i))
print('Index of a string (from Right side):', s.rindex(i))
print('-------------Slice Operator of string---------------')
print('Slice of a string:', s[0:5], '\n', s[1:15:2], '\n', s[::-1])
print('-------------Replication and Concatenation of string---------------')
print('Repeating of a string:', s * 2)
print(s + ' Ram')
print('-------------Finding a sub_string given string---------------')
print(s)
ch = input('Enter a character to find:')
if ch in s:
    print('ch is in s!')
else:
    print('ch is not in s!')

print('-------------Removing space using strip------------')
n = '       SRam      '
print(n)
a = n.rstrip()
print('Right strip :', a)
b = n.lstrip()
print('Left strip :', b)
c = n.strip()
print('Right and left strip :', c)
print('----------Finding a sub-string-------------------')
print('Finding ch in s(default from left side check):', s.find(ch))
print('Finding ch in s(check from Right side of s):', s.rfind(ch))
print('-------------Count of sub-string in string---------------')
print('Finding ch in s:', s.count(ch))
