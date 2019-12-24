n = int(input('Enter a number:'))
if n > 1:
    for i in range(2, n // 2 + 1):
        if (n % i) == 0:
            print(n, 'is not a prime')
            print(i, "times", n // i, 'is', n)
            break
    else:
        print(n, 'is a prime')
else:
    print(n, 'is not a prime')
print('=====================================================================')
lower = 1
upper = 10
print("Prime numbers between", lower, "and", upper, "are")
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num//2+1):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ')



