class AgeError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return self.message


try:
    age = int(input('Enter an age of yours: '))
    if age >= 18:
        print('Your are Eligible for Vote!')
    else:
        raise AgeError('Invalid Age', 'Your not Eligible for Vote!')

except Exception as e:
    print(e)
