# CSV means comma separated file
import csv

fname = input('Enter file name:')
with open(fname, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    feilds = []
    while True:
        barcode = int(input('Enter barcode number:'))
        pname = input('Enter product name:')
        price = input('Enter price:')
        feilds.append(barcode)
        feilds.append(pname)
        feilds.append(price)
        csv_writer.writerow(feilds)
        feilds.clear()
        opt = input('write another record[y/n]: ')
        if opt in ('n', 'N'):
            break
