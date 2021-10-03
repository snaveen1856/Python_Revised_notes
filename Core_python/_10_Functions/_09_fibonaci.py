def fibonaci(a):
    t1 = 0
    t2 = 1
    i = 1
    while i <= a:
        print(t1, end=' ')
        t1, t2 = t2, t1 + t2
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
