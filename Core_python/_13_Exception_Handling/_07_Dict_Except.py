class Name_not(Exception):

    def __init__(self, msg):
        self.msg = msg


class Value_not(Exception):

    def __init__(self, msg):
        self.msg = msg


try:
    d = {'Naveen': 1234, 'Sindhu': 1213, 'Sai': 1856, 'Chinni': 1729}
    name = input('Enter your name:')
    a = d.get(name, -1)
    if a == -1:
        raise Name_not('You do not have Account!')
    else:
        s = int(input('Enter a pin number:'))
        if s in d.values():
            b = d[s]
        else:
            raise Value_not('Value is not exit!')
    for i in d.items():
        print(i)

except Exception as e:
    print(e)
else:
    for i in d.items():
        print(i)
finally:
    print('Done')
