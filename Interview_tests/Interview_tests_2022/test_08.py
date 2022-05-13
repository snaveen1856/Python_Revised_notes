string = 'this is Ram'
words = string.split(' ')
req_words = [word[::-1] for word in words]
print(req_words)
res = ''

print(res)
for i in req_words:
    res = res + i + ' '
print(res)

