# Finding the numbers which are multiples of 5 and divided by 7 !
n = int(input('Enter a number to start from : '))
m = int(input('Enter a number to end : '))
for i in range(n, m):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=' ')
new_list = [i for i in range(n, m) if i % 7 == 0 and i % 5 == 0]
print("\nnew_list :", new_list)
