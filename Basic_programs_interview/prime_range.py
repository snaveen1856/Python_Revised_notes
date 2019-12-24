# print prime numbers range

low_limit = int(input('Enter an lower limit integer:'))
upp_limit = int(input('Enter a upper limit integer:'))
for n in range(low_limit, upp_limit + 1):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            break
    else:
        print(n, end=' ')
print()
