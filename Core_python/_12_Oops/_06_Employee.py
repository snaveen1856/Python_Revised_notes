class Employee:
    def __init__(self, empid, name, deportment, mail=''):
        self.empid = empid
        self.name = name
        self.dept = deportment
        self.mail = mail

    def getDeportment(self):
        return self.dept

    def setDeportment(self, deportment):
        self.dept = deportment

    def show(self):
        print('Employee id:', self.empid)
        print('Name:', self.name)
        print('Deportment:', self.dept)
        if self.mail:
            print('Mail:', self.mail)


class Manager(Employee):
    def __init__(self, empid, name, deportment, salary, mail=''):
        self.salary = salary
        Employee.__init__(self, empid, name, deportment, mail)

    def show(self):
        Employee.show(self)
        print('Employee salary:', self.salary)

    def getPay(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary

    def increment(self, rate):
        self.salary = self.salary + (self.salary * (rate / 100))


class ContractEmploy(Employee):
    def __init__(self, empid, name, deportment, rate, hours, mail=''):
        self.rate = rate
        self.hours = hours
        super().__init__(empid, name, deportment, mail)

    def getPay(self):
        return self.rate * self.hours

    def show(self):
        super().show()
        print("Rate :", self.rate)
        print("Hours:", self.hours)


class Salesman(ContractEmploy):
    def __init__(self, empid, name, sales, rate, hours, deportment='Sales', mail=''):
        self.sales = sales
        self.comm = Salesman.computeComm(sales)
        super().__init__(empid, name, deportment, rate, hours, mail)

    def computeComm(sales):
        sales -= 10000
        if sales <= 0:
            comm = 0.0
        elif sales <= 2500:
            comm = sales * 0.05
        elif sales <= 5000:
            comm = sales * .075
        else:
            comm = sales * 0.1
        return comm

    def getPay(self):
        return super().getPay + self.comm

    def getcomm(self):
        return self.comm

    def show(self):
        super().show()
        print('Sales:', self.comm)


s1 = Salesman(401, 'Siva', 15490, 450, 110)
s2 = Salesman(402, 'Sam', 12500, 456, 108, mail='sam1213@.com')
print(s1.getcomm())
print(s2.getcomm())
s1.show()
s2.show()

e = ContractEmploy(312, 'Divyasri', 'HR', 450, 120)
e.show()
print(e.getPay())
print(ContractEmploy.__mro__)

m1 = Manager(102, 'Ram', 'HR', 50000)
m1.show()
print(m1.getDeportment())
print(Manager.__mro__)
