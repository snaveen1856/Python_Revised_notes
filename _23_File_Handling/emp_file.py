""" create a file with employee and insert record into file system
"""
F_NAME = input('Enter file name: ')
try:
    FILE = open(F_NAME, 'w')
    while True:
        EMP_ID = input('Enter Employee id: ')
        NAME = input('Enter Employee name: ')
        JOB = input('Enter job: ')
        SALARY = int(input('Enter salary: '))
        REC = EMP_ID + ',' + NAME + ',' + JOB + ',' + str(SALARY) + '\n'
        FILE.write(REC)
        OPTION = input('Write another record: [y/n]:')
        if OPTION in ('n', 'N'):
            break

except Exception as exe:
    print(exe)
finally:
    if FILE:
        FILE.close()
