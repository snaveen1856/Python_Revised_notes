# multiplication table

t = int(input('Enter table number:'))
terms = int(input('Enter of terms of table:'))
i = 1
while i <= terms:
    print('{} X {} = {}'.format(t, i, (t * i)))
    i += 1
