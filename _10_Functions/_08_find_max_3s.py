def find_max(a, b, c):
    m = 0
    if a > b:
        m = a
    else:
        m = b
    if c > m:
        m = c
    print('Maximum of three numbers is:', m)


def Max_3(a, b, c):
    if a > b and a > c:
        print('Max:', a)
    elif b > a and b > c:
        print('Max:', b)
    else:
        print('Max:', c)


x = int(input('Enter a number x: '))
y = int(input('Enter a number y: '))
z = int(input('Enter a number z: '))
find_max(x, y, z)
Max_3(x, y, z)
print(Max_3(29, 46,79))
