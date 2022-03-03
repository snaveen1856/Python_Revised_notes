string = 'aaabccdaabcd'

#  abcdabcd
req = []
last_ele = string[0]
req.append(last_ele)
for char in string:
    if char != last_ele:
        req.append(char)
    last_ele = char
print(''.join(req))
