# printing fibonacci series

terms = int(input('Enter number of terms:'))
i = 1
t1 = 0
t2 = 1
while i <= terms:
    print(t1, end=' ')
    t1, t2 = t2, t1 + t2
    i += 1
print()

print("===============================")
a1 = 0
a2 = 1
for _ in range(terms):
    print(a1, end=' ')
    a1, a2 = a2, a1+a2
print()