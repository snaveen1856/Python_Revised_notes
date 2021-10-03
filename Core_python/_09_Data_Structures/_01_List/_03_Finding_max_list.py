import random

s = [random.randint(1, 100) for i in range(11)]
print("list of S= ", s)
maxy = 0
miny = 100
for i in s:
    if i > maxy:
        maxy = i
    continue
print("Maximum of list S: ", maxy)
for i in s:
    if i < miny:
        miny = i
    continue
print('Minimum of list S: ', miny)

# we code this functionality by Built-in Functions {max(s),min(s)}

print('Maximum of list S Using a Built-in Function: ', max(s))
print('Minimum of list S Using a Built-in Function: ', min(s))
