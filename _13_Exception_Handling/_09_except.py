try:
    n1 = int(input('Enter an integer:'))
    n2 = int(input('Enter an integer:'))
    result = n1 // n2
except ValueError as v:
    print('Enter a valid numbers:', v)
except ZeroDivisionError as zde:
    print('Zero division not possible:', zde)
except NameError as n:
    print('Enter a valid numbers:', n)
else:
    print(result)
finally:
    print('Done')
