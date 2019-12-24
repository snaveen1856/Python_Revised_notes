import csv

'''
import xlwt #to write excel(.xls) files

#Create a new workbook object
workbook = xlwt.Workbook()

#Add an excel sheet
worksheet = workbook.add_sheet('Coordinates')

#Add coordinate on each cell
for x in range(0, 5):
    for y in range(0, 5):
        value = str(x) + "," + str(y)
        worksheet.write(x, y, value)

#Save and create new excel file 
workbook.save('OutputFile.xls') '''

rows = [(1, 'Audi', 52642), (2, 'Mercedes', 57127), (3, 'Skoda', 9000),
        (4, 'Volvo', 29000), (5, 'Bentley', 350000)]

with open("C:/Users/manne/Desktop/out1.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['Datetime of Forecast',
                     'Forecasted Datetime',
                     'Forecasted LMP'])
    for row in rows:
        writer.writerow(row)
