import sys
import os
import psycopg2
import codecs

cmd1 = '/home/admin/sutas1122/Sutas_Logs'
print(cmd1)
dir_names = []
log_files = []
for (dirpath, dirname, filenames) in os.walk(cmd1):
    log_files.extend(filenames)
    dir_names.extend(dirname)
    # print(dirname)
print(dir_names[0])
# print(log_files)
cmd1 += '/' + dir_names[0] + '/' + 'report.html'
f = codecs.open(cmd1, 'r')
print(f.read())
data = f.read()
connection = None
try:
    connection = psycopg2.connect(
                        "dbname='gtaproject' host='10.10.1.10' user='gtauser' password='password'")
    cur = connection.cursor()
    # user_id = kwargs['dag_run'].conf['user_id']
    user_id = 1
    # test_name_log = data
    test = "test_log"
    insert_query = """ INSERT INTO authentication_executionstatus (user_id, key, value) VALUES (%s,%s,%s)"""
    record_to_insert = (user_id, test, data)
    cur.execute(insert_query, record_to_insert)
    connection.commit()
except psycopg2.DatabaseError as err:
    print("Error in DB inserting:", err)
    sys.exit(1)

finally:
    if connection:
        connection.close()
