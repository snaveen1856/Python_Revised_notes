n = int(input('Enter a integer: '))

for i in range(2, n // 2 + 1):
    if n % i == 0:
        print('It is not a Prime number')
        print(f'{i} times {n//i} equal {n}')
        break
else:
    print('It is a Prime number')
