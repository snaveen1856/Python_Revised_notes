def factorial(n):
    n = abs(n)
    while True:
        if n == 0 or n == 1:
            return 1

        if n > 1:
            return n * factorial(n - 1)


s = int(input('Enter a number: '))
k = factorial(s)
print("Factorial Using the recurring:", k)


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


p = factorial(6)
print(f'Factorial of {6}:', p)
