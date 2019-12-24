def factorial(n):
    n = abs(n)
    while True:
        if n == 0 or n == 1:
            return 1

        if n > 1:
            return n * factorial(n - 1)


s = int(input('Enter a number: '))
k = factorial(s)
print(k)
