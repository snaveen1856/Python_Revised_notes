import copy

x = """John is at a post, where they make pots. Making the pots will
stop in the future. Oh dear, what will happen to them when it 
happens. This can happen only in Rome, Read on to find more."""
words = []
for line in x.split('\n'):
    for w in line.split(' '):
        words.append(w)

s = set()
for x in words:
    if x:
        s.add(x)

fs = set()
for x in s:
    fs.add(x.lower().replace(".", "").replace(",", ""))

res = []
for x in fs:
    t = copy.deepcopy(fs)
    if x in t:
        t.remove(x)
    for y in t:
        if set(x) == set(y):
            res.append(y)

print(set(res))