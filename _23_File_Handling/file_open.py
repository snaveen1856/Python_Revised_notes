fname=input('Enter file name: ')
with open(fname) as f:
    data=f.readlines()
    for row in data:
        #row=row.rstrip('\n')
        feilds=row.split(',')
        feilds[-1]=feilds[-1].rstrip('\n')
        #print(row)
        print(feilds[0],feilds[1])
