# printing leap year

year = int(input('Enter an year:'))
if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
    print(year, 'is a Leap year')
else:
    print(year, 'is not a Leap year')
