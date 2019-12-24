import csv
#fname=input('Enter file name:')
#with open(fname) as csv_file:
   # csv_reader=csv.reader(csv_file)
    #for row in csv_reader:
       # print(row[0],row[1])

fname=input('Enter file name:')
feilds=['barcode','pname','price']
with open(fname) as csv_file:
    csv_reader=csv.DictReader(csv_file,feildname=feilds)
    for row in csv_reader:
        print(row['pname'],row['price'])
