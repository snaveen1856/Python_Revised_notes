def tables(n, t):
    """ here n is a multiplication table number
    and t is number of terms we want"""
    i = 1
    for i in range(t + 1):
        print(f"{n}*{i}=", n * i)


s = int(input('Enter a number: '))
k = int(input('Enter number of terms: '))
f = tables(s, k)
print(f)
