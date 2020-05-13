# print prime numbers range
"""
low_limit = int(input('Enter an lower limit integer:'))
upp_limit = int(input('Enter a upper limit integer:'))
for n in range(low_limit, upp_limit + 1):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            break
    else:
        print(n, end=' ')
print()
"""


def prime(n):
    marked = set()
    res = []
    for x in range(2, n + 1):
        if x not in marked:
            res.append(x)
        marked.update(range(x * x, n + 1, x))
    print('Marked set is:', marked)
    return f"All prime numbers up to {n} are: {res}"


