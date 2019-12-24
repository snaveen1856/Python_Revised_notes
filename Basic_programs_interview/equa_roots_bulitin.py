# built in function
while True:
    import math
    import cmath

    a = int(input('Enter coefficient of X^2:'))
    b = int(input('Enter coefficient of X:'))
    c = int(input('Enter coefficient of constant:'))
    d = b ** 2 - 4 * a * c
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
    elif d == 0:
        r1 = r2 = -b / (2 * a)
    else:
        r1 = (-b + cmath.sqrt(d)) / (2 * a)
        r2 = (-b - cmath.sqrt(d)) / (2 * a)
    print('Root1: ', r1)
    print('Root2: ', r2)
    otp = input('compute another Quadratic equation:[y/n]:')
    if otp == 'n':
        break
