# Writing a file(Bonus.txt) with only one file (name) as input

name = input('Enter file name bonus: ')
b = open(name, 'w')

# first it will create file with user give name then take input as filename

fname = input('Enter file name:')
with open(fname) as f:
    data = f.readlines()  # Here it will read data line by line
    for row in data:  # Here it make loop to read and separate the data into fields
        row = row.rstrip('\n')
        feilds = row.split(',')
        empid = feilds[0]
        job = feilds[2]
        salary = int(feilds[3])
        if job == 'Manager':
            bonus = round(0.25 * 12 * salary)
        if job == 'Salesman':
            bonus = round(0.20 * 12 * salary)
        if job == 'Clerk':
            bonus = round(0.15 * 12 * salary)
        rec = empid + ',' + job + ',' + str(salary) + ',' + str(bonus) + '\n'
        b.write(rec)
        print(rec)
        opt = input('Write another record [y/n]: ')
        if opt in ('n', 'N'):
            break
