def fibonaci(a):
    s = 0
    n = 1
    i = 1
    while i <= a:
        print(s, end=' ')
        s, n = n, n + s
        i += 1


def fibo(m):
    f = 0
    l = 1
    for i in range(m):
        print(f, end=' ')
        f, l = l, l + f


k = int(input('Enter number of terms: '))
fibonaci(k)
print('\n--------------------')
fibo(k)
