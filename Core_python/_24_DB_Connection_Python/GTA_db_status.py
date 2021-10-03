import psycopg2
import argparse
import sys
import json

"""
parser = argparse.ArgumentParser(description='parse key pairs into a dictionary')


class StoreDictKeyPair(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self._nargs = nargs
        super(StoreDictKeyPair, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        my_dict = {}
        print("values: {}".format(values))
        for kv in values:
            k, v = kv.split(":")
            my_dict[k] = v
        setattr(namespace, self.dest, my_dict)


parser.add_argument("--kv", dest="my_dict", action=StoreDictKeyPair, nargs="+", metavar="KEY:VAL")

args = parser.parse_args(sys.argv[1:])

"""

#
# parser = argparse.ArgumentParser()
# parser.add_argument('-i', '--input', help="JSON file to be processed")
# arguments = parser.parse_args()
# inp = ""
# if arguments.input:
#     # print(arguments.input, type(arguments.input))
#     inp = arguments.input
#     print(inp,type(inp))
# else:
#     print("usage: program -i <input json>")
#     sys.exit(-1)
# data_info = {}
# data = json.loads(inp)
# print(data)
# data = inp.replace("'{", '')
# data_0 = data.replace("}'", '')
# dict_data = data_0.split(",")
# for kv in dict_data:
#     k, v = kv.split(":")
#     data_info[k] = v
# print(data_info, type(data_info))
# record_to_insert = (data_info.get("user"), data_info.get("state"), data_info.get("status"))
# print(record_to_insert, type(record_to_insert))
"""
connection = None

try:
    connection = psycopg2.connect("dbname='gtaproject' host='10.10.1.10' user='gtauser' password='password'")
    cur = connection.cursor()
    postgres_insert_query = "INSERT INTO authentication_executionstatus (user_id, key, value) VALUES (%s,%s,%s)"
    # record_to_insert = (2, "status", "sucess")
    record_to_insert = (data_info.get("user_id"), data_info.get("state"), data_info.get("status"))
    cur.execute(postgres_insert_query, record_to_insert)
    connection.commit()

except psycopg2.DatabaseError as err:
    print(f"Error in DB inserting: {err}")
    sys.exit(1)
finally:
    if connection:
        connection.close()
"""

# python db_status.py -i '{"user": srikanththalla, "state":"GIT", "status":"Success"}'


import psycopg2
import argparse
import sys
# import pdb
import json

"""
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help="JSON file to be processed")
arguments = parser.parse_args()
inp = ""
if arguments.input:
    inp = arguments.input

else:
    print("usage: program -i <input json>")
    sys.exit(-1)
#pdb.set_trace()

data_info = {}
d=json.loads(inp)
#print(d)
data_info.update(d)"""


# print(data_info)

def write_db(ds, **kwargs):
    connection = None

    try:
        connection = psycopg2.connect("dbname='gtaproject1' host='10.10.1.10' user='gtauser' password='password'")
        cur = connection.cursor()
        user_id = kwargs['dag_run'].conf['user_id']
        state_git = kwargs['dag_run'].conf['state_git']
        status_git = kwargs['dag_run'].conf['status_git']
        # pdb.set_trace()
        insert_query = """ INSERT INTO authentication_executionstatus (user_id, key, value) VALUES (%s,%s,%s)"""
        record_to_insert = (user_id, state_git, status_git)
        cur.execute(insert_query, record_to_insert)
        connection.commit()
    except psycopg2.DatabaseError as err:
        print("Error in DB inserting:", err)
        sys.exit(1)

    finally:
        if connection:
            connection.close()


git_status = PythonOperator(task_id='git_status', provide_context=True, python_callable=write_db, dag=dag)
