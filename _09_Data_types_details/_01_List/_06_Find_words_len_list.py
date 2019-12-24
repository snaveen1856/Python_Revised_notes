s = ['blue', 'white', 'red', 'black', 'brown', 'green', 'orange', 'pink', 'violet', 'rose', 'lilly',
     'jasmine', 'lotus', 'lion', 'tiger', 'monkey', 'donkey', 'elephant', 'crocodile', 'fox', 'dog',
     'horse', 'cat']
l = []
for item in s:
    if len(item) >= 6:
        l.append(item)

print(l)
for a in '012':
    # print(a,type(a))
    i = int(a)
    l.pop(i)
print(l)
# l.pop(0)
print(l)
