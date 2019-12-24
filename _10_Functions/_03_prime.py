def prime(n):
    for i in (2, n // 2 + 1):
        if n % i == 0:
            print('It is not a Prime!')
            break
    else:
        print('It is a Prime!')


x = int(input('Enter a number: '))
prime(x)
print(prime(256))
