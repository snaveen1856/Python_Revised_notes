d = {'a': 2, 'b': 3}
s = str(d)
print(s, type(s))
e = eval(s)
print(e)

lst = [1, 3, 5, 7]
maxn = 0
for ele in lst:
    if ele > maxn:
        maxn = ele
    else:
        maxn = maxn
