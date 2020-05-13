# using Recursive function factorial
def fact(n):
    if n in (0, 1):
        return 1
    return n * fact(n - 1)


a = int(input('Enter an integer:'))
factorial = fact(a)
print(f"{a} factorial is {factorial}")

f = 1
if a in (1, 0):
    print('factorial using for logic:', 1)
else:
    for i in range(1, a + 1):
        f = f * i
    print('factorial using for loop:', f)
