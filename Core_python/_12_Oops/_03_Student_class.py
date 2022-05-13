class Student:
    college = 'IIT-Madras'
    scount = 0

    def __init__(self, rollno, name, course, fee, test):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.fee = fee
        self.test = test
        Student.scount += 1

    def __str__(self):
        return f"{self.rollno}-{self.name}-{self.course}-{self.fee}-{self.test}"

    def is_pass(self):
        if self.test >= 45:
            print(f"{self.rollno}--{self.name}--{self.test}: Pass")
        else:
            print(f"{self.rollno}--{self.name}--{self.test}: Fail")

    def fee_paid(self):
        if self.course in ('Python', 'Java'):
            if self.fee == 10000:
                print('You paid course completely:', self.fee)
            else:
                print('You have to pay remaining amount is: ', (10000 - self.fee))
        else:
            if self.fee == 15000:
                print('You paid course fee completely:', self.fee)
            else:
                print('You have to pay remaining amount is: ', (15000 - self.fee))

    @classmethod
    def get_college(cls):
        return f"College Name: {Student.college}   Count student:{Student.scount}"


try:
    navn = Student(101, 'Ram', 'Python', 10000, 98)
    sai = Student(102, 'Sai B', 'Python', 9000, 96)
    sam = Student(103, 'Sam N', 'Java', 10000, 56)
    john = Student(104, 'John', 'Data Science', 15000, 31)
    smith = Student(105, 'Smith', 'Data Science', 10000, 35)
    sunder = Student(106, 'Sunder', 'Java', 8000, 30)
    navn.is_pass()
    sai.is_pass()
    sam.is_pass()
    john.is_pass()
    smith.is_pass()
    sunder.is_pass()
    print('-' * 40)
    print(navn)
    print(sai)
    print(sam)
    print(john)
    print(smith)
    print(sunder)
    print(Student.get_college(), "\n", type(Student.get_college()))
    navn.fee_paid()
    sai.fee_paid()
    sam.fee_paid()
    smith.fee_paid()
    sunder.fee_paid()
    john.fee_paid()
    ram = Student(1025, 'Ram')
    print(ram)
    don = Student('152', 5658, 'Py', 4587, 94)
    print(don)
    print(don.is_pas)
except Exception as e:
    print('Exception Handled well:', e)
finally:
    print('Done')
