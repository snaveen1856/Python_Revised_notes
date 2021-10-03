try:
    n1 = int(input('Enter an integer:'))
    n2 = int(input('Enter an integer:'))
    result = n1 // n2
    print(result)
# print('Result:',result)

# except(ValueError):
# print('Enter valid number only:')
except ZeroDivisionError:
    print('Divide by zero')
# except NameError as ne:
# print(ne)
# except(Exception) as e:
# print(e)

# else:
# print('Result:', result)

finally:
    print('Done')
