def prime(n):
    if n > 1:
        for i in (2, n // 2 + 1):
            if n % i == 0:
                print(f'{n} is not a Prime! ')
                break
        else:
            print(f'{n} is a Prime!')
    else:
        print('Entered number is less than or equal to 1')


x = int(input('Enter a positive number: '))
prime(x)
prime(256)
