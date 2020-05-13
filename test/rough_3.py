import random as rn

# Python program to check
# if a string is palindrome
# or not

x = "malayalam"
w = ""
for i in x:
    w = i + w
if x == w:
    print("YES")
print('----------------- Patterns ----------------------------')
n = 5
for idx in range(n - 1):
    print((n - idx) * ' ' + (2 * idx + 1) * '*')
for idx in range(n - 1, -1, -1):
    print((n - idx) * ' ' + (2 * idx + 1) * '*')
print('---------------------------------------------')
l = [rn.randint(1, 50) for i in range(10)]
print("list l=", l)
rev_l = l.reverse()
s = [2 * i for i in l if i % 2 == 0]
print('Doubled the even number s=', s)
print('===============================================')
g = (2 * i for i in range(10))
print(g, type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print("=========================================================")

"""
def prime():
    num = int(input('Enter a number to check prime or not :'))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print('Entered number is not prime', num)
            # print(num, 'is not a prime number' if num % i == 0 else 'is a prime number')
                break
        else:
            print('entered number is prime')
    else:
        print('please enter a number greater than 1')

prime()
"""
n = input('Enter a number:')
w = ''
num_sum = 0
for i in n:
    w = i + w
    i = int(i)
    num_sum += i
print(w)
print(num_sum)
