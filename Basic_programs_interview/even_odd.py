# printing even or odd

n = int(input('Enter a number:'))
if n % 2:
    print(n, 'is Odd')
else:
    print(n, 'is Even')

# n=int(input('Enter a number:'))
# if n%2==0:
# print(n,'is Even')
# else:
#  print(n,'is Odd')

for i in range(10, 100):
    for k in range(2, (i // 2) + 1):
        if i % k == 0:
            break
    else:
        print(i, end=' ')
