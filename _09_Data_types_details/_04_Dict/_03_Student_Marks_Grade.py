""" Student data store in dict and process to find Grade
"""
marks = dict()
class_10 = '10_Std'
while True:
    name = input('Enter name:')
    if not name:
        break
    m = int(input('Enter marks:'))
    marks[name] = m
'''    opt=input('Do you want enter another record:[y/n]: ')
    if opt in ('n','N'):
        break'''
sum = 0
for i in marks.items():
    sum += i[1]
    # print(i)
marks[class_10] = sum
print(sum)
print(marks.items())
'''
while True:
    name=input('Enter name to search:')
    m=marks.get(name,-1)
    if m== -1:
        print(name,'not found')
    else:
        print(f"{name} marks :{m}")
        opt = input('search another student [y/n]:')
        if opt in ('n', 'N'):
            #for k in sorted(marks.keys()):
                #print(k,':',marks[k])
            break

'''
