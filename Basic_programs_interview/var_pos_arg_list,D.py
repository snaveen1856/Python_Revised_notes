# variable positional argument function with necessary argument,tuple and dictionary
# Here it will create tuple for *n and dictionary for **orgs


def add(x, y, *n, **k):
    total = x + y
    if n:
        print('These are elements come under in tuple:', n)
        for i in n:
            total += i
    if k:
        print('These are elements come under in Dict:', k)
        for i in k.values():
            total += i
    return f"Sum of all items:", total


t = add(4, 5, 68, 18, a=56, b=12, c=13)
print(t)
t = add(18, 56, a=12, b=13, c=20, d=3)
print(t)
