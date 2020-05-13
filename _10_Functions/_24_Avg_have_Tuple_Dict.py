# variable positional argument function with necessary argument,tuple and dictionary
def add(x, y, *n, **k):  # Here it will create tuple for *n and dictionary for **kwargs
    total = x + y
    if n:
        for i in n:
            total += i
    if k:
        for i in k.values():
            total += i
    return total


t = add(4, 5, 68, 18, a=56, b=12, c=13)
print('Sum of all item in Tuple and Dict:', t)
t = add(18, 56, a=12, b=13, c=20, d=3)
print('Sum of all item in Tuple and Dict:', t)
