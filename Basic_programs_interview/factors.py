# Factors of given number

n = int(input('Enter a integer:'))
for i in range(1, n // 2 + 1):
    if n % i == 0:
        print(i, end=',')
print(n)
