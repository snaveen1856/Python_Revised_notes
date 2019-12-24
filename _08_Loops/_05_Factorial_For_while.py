# Factors of given number using for loop and while loop

n = int(input('Enter a integer:'))
for i in range(1, n // 2 + 1):
    if n % i == 0:
        print(i, end=' ')

print(n)

'''
i=1
while i <= n//2:
    if n%i == 0:
        print(i,end=' ')
    i +=1
print(n)    '''
