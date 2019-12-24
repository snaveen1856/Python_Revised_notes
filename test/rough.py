"""
####### Prime number  #######

n = int(input('Enter a number:'))
if n > 1:
    for i in range(2, n // 2 + 1):
        if (n % i) == 0:
            print(n, 'is not a prime')
            print(i, "times", n//i, 'is', n)
            break
    else:
        print(n, 'is a prime')
else:
    print(n, 'is a prime')
"""

"""
lower = int(input("Enter lower range:"))
upper = int(input("Enter upper range:"))
print('prime number between', lower, 'and', upper)
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, ',', end='')
"""

#####    Python program to display all the prime numbers within an interval    ########


lower = 1
upper = 20
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

"""
##### Factors #####
def print_factor(x):
    print('The factors of ', x, 'are:')
    for i in range(1, x//2 + 1):
        if x % i == 0:
            print(i, ',', end='')
    else:
        print(x)


num = 36
print_factor(num)
"""

"""
def compute_hcf(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


num1 = 52
num2 = 24
print(num1, 'and', num2, 'H.C.F is:', compute_hcf(num1, num2))"""

"""
# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

hcf = compute_hcf(52, 24)
print("The HCF is:", hcf)
"""
"""# Sum of natural numbers up to num
num = 10
if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate until zero
    while num > 0:
        sum += num
        num -= 1
    print("The sum is:", sum)
    """

# Program to check Armstrong numbers in a certain interval
lower = 100
upper = 2000
for num in range(lower, upper + 1):
    # order of number
    order = len(str(num))

    # initialize sum
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10

        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)
