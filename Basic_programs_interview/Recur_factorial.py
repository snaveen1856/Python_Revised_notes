# using Recursive function factorial
def fact(n):
    if n in (0, 1):
        return 1
    return n * fact(n - 1)


a = int(input('Enter an integer:'))
factorial = fact(a)
print(f"{a} factorial is {factorial}")
