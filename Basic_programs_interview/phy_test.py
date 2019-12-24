# selecting person in physical test

gender = input('Enter Gender:')
height = float(input('Enter height:'))
age = int(input('Enter Age:'))
if gender == 'female' and height >= 5.4 and 23 <= age <= 30:
    print('selected')
elif gender == 'male' and height >= 5.6 and 24 <= age <= 32:
    print('selected')
else:
    print('Not selected')
