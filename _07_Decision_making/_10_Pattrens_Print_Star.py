n = int(input('Enter a number of rows:'))

blank = 40
for i in range(1, n + 1):
    print(' ' * blank, end='')
    for j in range(1, i + 1):
        print('*', end='')
    print()
    blank -= 1
print('--------------------------------------------------')
for row in range(1, n + 1):
    for col in range(1, n - row + 1):
        print(' ', end='')
        # print(end=" ")
    for col in range(row, 0, -1):
        print('*', end='')
    for col in range(2, row + 1):
        print('*', end='')
    print()
print('-------------------------------------------------')
for row in range(1, n + 1):
    for col in range(1, n - row + 1):
        print(' ', end='')
        # print(end=" ")
    for col in range(row, 0, -1):
        print(col, end='')
    for col in range(2, row + 1):
        print(col, end='')
    print()
print('=================================================')
for idx in range(n-1):
    print((n-idx) * ' ' + (2*idx+1) * '*')
for idx in range(n-1, -1, -1):
    print((n-idx) * ' ' + (2*idx+1) * '*')