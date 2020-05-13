def tables(n, t):
    """ here n is a multiplication table number
    and t is number of terms we want"""

    for i in range(1, t + 1):
        print(f"{n} X {i} =", n * i)


s = int(input('Enter a number: '))
k = int(input('Enter number of terms: '))
tables(s, k)

