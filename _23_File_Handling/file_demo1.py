fname = input('Enter file name: ')
try:
    f = open(fname, 'a')
    while True:
        sid = input('Enter student id: ')
        name = input('Enter student name: ')
        course = input('Enter course: ')
        rec = sid + ',' + name + ',' + course + '\n'
        f.write(rec)
        opt = input('Write another record: [y/n]:')
        if opt in ('n', 'N'):
            break

except Exception as e:
    print(e)
finally:
    if f:
        f.close()
