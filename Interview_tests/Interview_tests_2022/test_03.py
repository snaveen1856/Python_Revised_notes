import csv

# with open('sample.csv', 'r+') as fname:
#     fdata = fname.readlines()
#     with open('result.csv', 'w+') as res:
#         for row in fdata:
#             if 'ingress' in row:
#                 print(row, type(row))
#                 req_row = row.split(',')
#                 res_lst = (req_row[1], req_row[0],req_row[2], req_row[3])
#                 res.writelines(res_lst)
#             else:
#                 # res.writelines(row)
#                 res_lst = (req_row[1], req_row[0], req_row[2], req_row[3])
#                 res.writelines(res_lst)
from django.http import HttpResponse

import datetime


def today_date():
    t_date = datetime.datetime.today()
    print(t_date)
    return HttpResponse(f'<html><h1>{t_date}</h1></html')


today_date()
