import psycopg2
import csv

con = psycopg2.connect(database='postgres', user='postgres', password='naveen1213')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()
    # print(rows)   # for testing output
    # for row in rows:      # for testing output from DB
    # print(f"{row[0]} {row[1]} {row[2]}")

with open("C://Users//naveen.kuruva//Desktop//out2.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['S.NO',
                     'Car Name',
                     'Model'])
    for row in rows:
        writer.writerow(row)
print('Writing data from DB to Excel file: "SUCCESS"')
