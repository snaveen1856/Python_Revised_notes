class Not_int(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Int_list(list):

    def append(self, value):
        if isinstance(value, int):
            super().append(value)
        else:
            raise Not_int('We are in APPEND methodOnly integer vales are allowed:')

    def insert(self, index, value):
        if isinstance(value, int):
            super().insert(index, value)
        else:
            raise Not_int('We are in INSERT method Only integer vales are allowed:')

    def extend(self, n):
        k = []
        if type(n) is list: # if isinstance(n, list):
            for i in n:
                if isinstance(i, int):
                    k.append(i)
        super().extend(k)


try:
    ilist = Int_list()
    ilist.append(10)
    ilist.append(20)
    ilist.append(30)
    ilist.append(40)
    ilist.append(50)
    # ilist.append('abc')
    ilist.append(90)
    ilist.insert(1, 80)
    # ilist.insert(1, 'abc')
    s = [1, 2, 3]
    # print(s)
    ilist.extend(s)
except Not_int as e:
    print(e)
finally:
    print("List only  allowed int:", ilist)
