"""
d={'Ram':1234,'Divyasri':1213,'Sai':1856,'madhu':1729}
name=input('Enter your name:')
a=d.get(name,-1)
if a==-1:
    print('You do not have Account:')
    break
else:
    s=int(input('Enter a pin number:'))
    if s in d.values():
        b=d[s]
def with_draw(a):

"""


class Account:
    bank = 'SBI'
    branch = 'Bengalure'
    acc_count = 0
    d = {'Ram': 1234, 'Divyasri': 1213, 'Sai': 1856, 'madhu': 1729}

    def __init__(self, acc_no, name, bal=500):
        self.acc_no = acc_no
        self.name = name
        self.bal = bal
        Account.acc_count += 1

    def __str__(self):

        return f"{self.acc_no}:{self.name}:{self.bal}"

    def credit(self, amt):
        self.bal += amt
        return self.bal

    def debit(self, amt):
        name = input('Enter your name:')
        a = Account.d.get(name, -1)
        if a == -1:
            print('You do not have Account:')
        else:
            s = int(input('Enter a pin number:'))
            if s in Account.d.values():
                if 500 < self.bal - amt:
                    self.bal -= amt
                    return f"{self.acc_no}-{self.name}-{self.bal}"
                else:
                    return 'Insufficent Balance'

    @classmethod
    def get_bank(cls):
        return print(Account.bank, ':', Account.branch, ':', Account.acc_count)


navn = Account(102, 'Ram', 10000)
sindu = Account(103, 'Divyasri', 15000)
navn.credit(5000)
navn.debit(12000)

# print(navn)
# sindu.debit(5000)
# print(sindu)
print(navn)