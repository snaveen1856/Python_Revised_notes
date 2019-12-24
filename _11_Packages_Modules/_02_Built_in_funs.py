import random
import cmath
import math
import time


def dice_game():
    system_option = random.randint(0, 6)
    print('System rolled value: ', system_option)
    opt1 = input('Do you want to play game:[y/n]: ')
    if opt1 in ('y', 'Y'):
        yours_option = random.randint(0, 6)
        print('You rolled value: ', yours_option)
    if system_option > yours_option:
        print('You lose game!')
    else:
        print("You won game!")


def exp(a, b):
    return math.ldexp(a, b)


def fact(n):
    return math.factorial(n)


def square_root(n):
    return math.sqrt(n)


def sin(k):
    return math.asin(k)


def cos(i):
    return math.acos(i)


def comp_rect(a, b):
    return cmath.rect(a, b)


def comp_polar(n):
    return cmath.polar(n)


def current_time():
    return time.localtime()


# a=int(input('Enter a value: '))
# b=int(input('Enter b value: '))
# print(f"{a}x{2}^{b}= ",exp(a, b))
# print('\n'f"Factorial of {a}!= ",fact(a))
# print('Complex Rectangular formate: ',comp_rect(a,b))
z = complex(input('Enter a complex number:'))
print('Complex of polar:', comp_polar(z))
