# using FILTER function

emp = "101,Ram,manager,50000,10"
fields = emp.split(',')
print(fields)
num_fields = list(filter(str.isdigit, fields))
print('num_fields:', num_fields)

emp = "102,Divyasri,manager,45000,10"
l = list(filter(str.isdigit, emp.split(',')))
print(emp.split(','))
l1 = list(map(int, l))
print('l1: ', l1)
