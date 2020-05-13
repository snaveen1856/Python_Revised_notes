from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators import PythonOperator

import psycopg2
import sys
import os
from jinja2 import Template
from datetime import datetime, timedelta
import time
import codecs


def log_file_status(ds, **kwargs):
    cmd1 = '/home/admin/GTA_logs/Sutas_logs'
    dir_names = []
    log_files = []
    for (dirpath, dirname, filenames) in os.walk(cmd1):
        log_files.extend(filenames)
        dir_names.extend(dirnames)

    cmd1 += '/' + dir_names[0] + '/' + 'report.html'
    f = codecs.openc(cmd1, 'r')
    data = f.read()

    connection = None
    try:
        connection = psycopg2.connect("dbname='gtaproject1' host='10.10.1.10' user='gtauser' password='password'")
        cur = connection.cursor()
        user_id = kwargs['dag_run'].conf['user_id']
        test = 'test_log'
        insert_query = """ INSERT INTO authentication_executionstatus (user_id, key, value) VALUES (%s,%s,%s) """
        record_to_insert = (user_id, test, data)
        cur.execute(insert_query, record_to_insert)
        connection.commit()
    except psycopg2.DatabaseError as err:
        print("Error in DB inserting:", err)
        sys.exit(1)


with DAG(dag_id='GTA_exec03', schedule_interval=None, start_date=datetime(2020, 3, 20), catchup=False) as dag:
    # task 1 testing purpose
    dummy_task = DummyOperator(task_id='dummy_task')

    # task 2 specified test case running
    test_case = BashOperator(task_id='test_case',
                             bash_command='/pushd /home/admin/gta_scripts && ./sutas_test_run.sh ' '{{dag_run.conf['
                                          '"containername"]}} {{dag_run.conf["testcase"]}}')

    # task 3 get log from docker daemon
    get_log_fm_docker = BashOperator(task_id='get_log_fm_docker',
                                     bash_command='pushd /home/admin/gta_scripts && ./sutas_logs.sh ' '{{dag_run'
                                                  '.conf["containername"]}}')

    # task 4 get log and update to DB
    log_file_status = PythonOperator(task_id='log_status', provide_context=True, python_callable=log_file_status)

    dummy_task >> test_case >> get_log_fm_docker >> log_file_status
