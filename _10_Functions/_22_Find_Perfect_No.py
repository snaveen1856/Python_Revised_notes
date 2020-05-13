def find_perf(n):
    s = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            print(f"Factor of number {n}: ", i)
            s += i
    if s == n:
        print('sum=', s)
        print('Given number is a Perfect number: ', n)
    else:
        print('sum of factors =', s)
        print('It is not a perfect number: ', n)


f = int(input('Enter a number to check: '))
find_perf(f)
