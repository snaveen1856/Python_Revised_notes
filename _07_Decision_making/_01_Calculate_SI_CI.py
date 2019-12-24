p = int(input('Enter a Principle amount:'))
t = int(input('Enter Time period in month:'))
r = int(input("Enter a rate of interest in Percentage:"))
print('\nSimple Interest Calculation!')
t = t / 12
# Si=0
Si = (p * t * r) / 100
# A=0
A = Si + p
print('Simple Interest:', Si)
print('Total Amount:', A)
print('-' * 40)
a = (1 + (r / 100)) ** t
Ci = p * (a - 1)
print('Compound Interest:', Ci)
print('Total Amount:', p + Ci)
