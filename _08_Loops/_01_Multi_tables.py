# Multiplication table printing

t = int(input('Enter a Multiplication table number: '))
terms = int(input('Enter number of terms: '))
i = 1
while terms >= i:
    print(f"{t}x{i}={t * i}")
    i += 1
