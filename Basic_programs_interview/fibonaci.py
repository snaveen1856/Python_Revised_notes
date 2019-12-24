# printing fibonacci series
terms = int(input('Enter number of terms:'))
i = 1
t1, t2 = 0, 1
print('---------Using while loop------------')
while i <= terms:
    print(t1, end=' ')
    t1, t2 = t2, t1 + t2
    i += 1
print()
print('------------Using For loop-------------')
a1, a2 = 0, 1
for j in range(1, terms + 1):
    print(a1, end=' ')
    a1, a2 = a2, a1 + a2
print()
