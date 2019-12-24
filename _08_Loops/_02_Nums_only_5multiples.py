# entered number is divisible with 5 or not
n = int(input('Enter a range of numbers: '))
i = 1
print('Numbers multiples of 5: ')
while n >= i:
    if i % 5 == 0:
        print(i, end=' ')

    i += 1
    continue
