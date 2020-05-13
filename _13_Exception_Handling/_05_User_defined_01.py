class Name_Error(Exception):

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


try:
    l = []
    while True:
        name = input('Enter a name:')
        if name:
            l.append(name)
        else:
            raise Name_Error('Name error', 'Enter a Alphabets only!')
except Exception as e:
    print(e)

finally:
    print('Names List:', l)
