# create a file with employee
fname = input('Enter file name: ')
try:
    f = open(fname, 'w')
    while True:
        empid = input('Enter Employee id: ')
        name = input('Enter Employee name: ')
        job = input('Enter job: ')
        salary = int(input('Enter salary: '))
        rec = empid + ',' + name + ',' + job + ',' + str(salary) + '\n'
        f.write(rec)
        opt = input('Write another record: [y/n]:')
        if opt in ('n', 'N'):
            break

except Exception as e:
    print(e)
finally:
    if f:
        f.close()
