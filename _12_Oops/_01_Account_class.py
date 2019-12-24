class Account:
    bank = 'SBI'
    branch = 'Bengalure'
    acc_count = 0

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

        if 500 < self.bal - amt:
            self.bal -= amt
            return self.bal
        else:
            return 'Insuffient Balance'

    @classmethod
    def get_bank(cls):
        return print(Account.bank, ':', Account.branch, ':', Account.acc_count)


'''        
naveen=Account(10210,'Naveen',5000) 
naveen.credit(5000)
smith=Account(10211,'Smith',6000) 
sai=Account(10212,'Sai',10000) 
raj=Account(10213,'Raj',7000) 
sam=Account(10214,'Sam',6000) 
john=Account(10215,'John',8000) 
jack=Account(10216,'Jack',9000) 
vijay=Account(10217,'Vijay',4000) 

#print(type(naveen))
print(naveen)
print(sai)
print(sam)
sai.debit(1000)
print(sai)
sam.debit(2000)
print(sam)
Account.get_bank()
#n1.get_acc_details()
#print(n1) 
sam.debit(2000)
print(sam)
'''
sam = Account(1021, "SAM", 5000)
print(sam)
sam.debit(6000)
print(sam)
sam.debit(2000)
print(sam)
