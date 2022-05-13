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


# sql_alchemy_conn = sqlite:////home/admin/airflow/airflow.db
# def clear_dag():
# import sqlite3


#   conn = sqlite3.connect('../airflow.db')
#    cur = conn.cursor()

#    dag_input = sys.argv[1]

#    for t in ["xcom", "task_instance", "sla_miss", "log", "job", "dag_run", "dag" ]:
#        query = "delete from {} where dag_id='{}'".format(t, dag_input)
#       cur.execute(query)

#  conn.commit()
# conn.close()

def list_out_files(ds, **kwargs):
    # git_dir=kwargs['dag_run'].conf['pro_dire']
    path = '/home/admin/GTA_ref_repo/tests/'
    test_suite = [test for test in os.listdir(path) if test.endswith('.robot')]
    connection = None
    try:
        connection = psycopg2.connect("dbname='gtaproject1' host='10.10.1.10' user='gtauser' password='password'")
        cur = connection.cursor()
        user_id = kwargs['dag_run'].conf['user_id']
        test_suites = {}
        for n, testname in enumerate(test_suite):
            test = "Test" + str(n)
            # test_suites[test]=testname
            # n = str(n)
            insert_query = """ INSERT INTO authentication_testsuite(user_id,key,value) VALUES(%s,%s,%s)"""
            record_to_insert = (user_id, n, testname)
            cur.execute(insert_query, record_to_insert)
            connection.commit()
    except psycopg2.DatabaseError as err:
        print("Error in DB inserting:", err)
        sys.exit(1)
    finally:
        if connection:
            connection.close()


def write_db_git(ds, **kwargs):
    connection = None

    try:
        connection = psycopg2.connect("dbname='gtaproject1' host='10.10.1.10' user='gtauser' password='password'")
        cur = connection.cursor()
        user_id = kwargs['dag_run'].conf['user_id']
        state = "GIT"
        status = "SUCCESS"
        # pdb.set_trace()
        insert_query = """ INSERT INTO authentication_executionstatus (user_id, key, value) VALUES (%s,%s,%s)"""
        record_to_insert = (user_id, state, status)
        cur.execute(insert_query, record_to_insert)
        '{"git_dire":"/home/admin/git_script/Pro_repo","git_url":"https://github.com/sRam1856/GTA_ref_repo.git",' \
        '"pro_dire":"/home/admin/git_script/Pro_repo/GTA_ref_repo/","imagename":"sutas01:v01",' \
        '"containername":"sutas01","testcase":"sutas_test.py"} '

        record_to_insert = (user_id, state, status)
        cur.execute(insert_query, record_to_insert)
        connection.commit()
    except psycopg2.DatabaseError as err:
        print("Error in DB inserting:", err)
        sys.exit(1)

    finally:
        if connection:
            connection.close()


def write_db_doc(ds, **kwargs):
    connection = None

    try:
        connection = psycopg2.connect("dbname='gtaproject1' host='10.10.1.10' user='gtauser' password='password'")
        cur = connection.cursor()
        user_id = kwargs['dag_run'].conf['user_id']
        state = "DOCKER"
        status = "UP"
        # pdb.set_trace()
        insert_query = """ INSERT INTO authentication_executionstatus (user_id, key, value) VALUES (%s,%s,%s)"""
        record_to_insert = (user_id, state, status)
        cur.execute(insert_query, record_to_insert)
        connection.commit()
    except psycopg2.DatabaseError as err:
        print("Error in DB inserting:", err)
        sys.exit(1)

    finally:
        if connection:
            connection.close()


def write_db_run(ds, **kwargs):
    connection = None

    try:
        connection = psycopg2.connect("dbname='gtaproject1' host='10.10.1.10' user='gtauser' password='password'")
        cur = connection.cursor()
        user_id = kwargs['dag_run'].conf['user_id']
        state = "DOCKER CONTAINER"
        status = "RUNNING"
        # pdb.set_trace()
        insert_query = """ INSERT INTO authentication_executionstatus (user_id, key, value) VALUES (%s,%s,%s)"""
        record_to_insert = (user_id, state, status)
        cur.execute(insert_query, record_to_insert)
        connection.commit()
    except psycopg2.DatabaseError as err:
        print("Error in DB inserting:", err)
        sys.exit(1)

    finally:
        if connection:
            connection.close()


def params_update(ds, **kwargs):
    profileInfo_values = list(
        [kwargs['dag_run'].conf["raisebugs"], kwargs['dag_run'].conf["jiraenv"], kwargs['dag_run'].conf["loglevel"],
         kwargs['dag_run'].conf["slack"], kwargs['dag_run'].conf["emailnotifications"],
         kwargs['dag_run'].conf["symmetrickey"], kwargs['dag_run'].conf["teamsnotifications"],
         kwargs['dag_run'].conf["consolidatedmail"], kwargs['dag_run'].conf["enabledatabase"],
         kwargs['dag_run'].conf["enabletestmanagement"], kwargs['dag_run'].conf["enablepushtestartifacts"]])

    profileInfo_keys = list(
        ["raisebugs", "jiraenv", "loglevel", "slack", "emailnotifications", "symmetrickey", "teamsnotifications",
         "consolidatedmail", "enabledatabase", "enabletestmanagement", "enablepushtestartifacts"])

    profileInfo = {element[0]: element[1] for element in zip(profileInfo_keys, profileInfo_values)}

    orginal = ['raisebugs', 'jiraenv', 'loglevel', 'slack', 'emailnotifications', 'symmetrickey', 'teamsnotifications',
               'consolidatedmail', 'enabledatabase', 'enabletestmanagement', 'enablepushtestartifacts']
    exp = list(profileInfo.keys())
    diffls = list(set(orginal) - set(exp))
    if len(diffls) == 0:
        pass
    else:
        print('missed json keys:', diffls)
        sys.exit(-1)
        ref_path0 = kwargs['dag_run'].conf["ref_path"]
        ref_path = str(ref_path0)
        ref_path = ref_path + '/' + 'test_template'
        # print(path)
    if os.path.isfile(ref_path):
        tm = Template(open(ref_path).read())
        file = tm.render(profileInfo)
        doc = open('/home/admin/GTA_ref_repo/sutas_test.py', 'w')
        succ = doc.write(file)
        # print('hi')
        # sys.exit(0)
    else:
        # print('hello')
        sys.exit(1)


now = time.localtime()
str_now = time.strftime("%M", now)
name = "GTA_dag"
name = name + str_now
GT = f"{name}"

with DAG(dag_id='GTA_pro_confg10', schedule_interval=None, start_date=datetime(2020, 3, 20),
         catchup=False) as dag:
    # Task 1 testing purpose
    dummy_task = DummyOperator(task_id='dummy_task')

    # Task 2 making dir
    bash_dir = BashOperator(task_id='bash_dir',
                            bash_command='pushd /home/admin/gta_scripts && ./create_dir.sh ' '{{dag_run.conf['
                                         '"git_dire"]}}')

    # Task 3 git clone project
    bash_git = BashOperator(task_id='bash_git',
                            bash_command='pushd /home/admin/gta_scripts && ./git_clone.sh ' '{{dag_run.conf['
                                         '"git_dire"]}} {{dag_run.conf["git_url"]}} ')

    # Task 4 change branch of git bash_ch_branch=BashOperator(task_id='bash_ch_branch',bash_command='pushd
    # /home/admin/gta_scripts && ./change_branch.sh ' '{{dag_run.conf["pro_dire"]}} {{dag_run.conf["git_branch"]}} ')

    # Task 5 Give status of Git clone git_status=BashOperator(task_id='git_status',bash_command='pushd
    # /home/admin/gta_scripts && python db_status_git.py -i ' '{{dag_run.conf["user_id"]}} {{dag_run.conf[
    # "state_git"]}} {{dag_run.conf["status_git"]}}')

    git_status = PythonOperator(task_id='git_status', provide_context=True, python_callable=write_db_git)

    # Task 6 ping the server
    ping_ser = BashOperator(task_id='ping_ser', bash_command='pushd /home/admin/gta_scripts && ./ping.sh ')

    # Task 7 params update params_update=BashOperator(task_id='params_update',bash_command='pushd
    # /home/admin/gta_scripts && python sutas_params_update.py -i ' '{{dag_run.conf["raisebugs"]}} {{dag_run.conf[
    # "jiraenv"]}} {{dag_run.conf["loglevel"]}} {{dag_run.conf["slack"]}} {{dag_run.conf["emailnotifications"]}} {{
    # dag_run.conf["symmetrickey"]}} {{dag_run.conf["teamsnotifications"]}} {{dag_run.conf["consolidatedmail"]}} {{
    # dag_run.conf["enabledatebase"]}} {{dag_run.conf["enabletestmanagement"]}} {{dag_run.conf[
    # "enablepushtestartifacts"]}} -d {{dag_run.conf["ref_path"]}} ')

    docker_params_update = PythonOperator(task_id='docker_params_update', provide_context=True,
                                          python_callable=params_update)

    # Task 8 docker build
    docker_build = BashOperator(task_id='docker_build', bash_command='pushd /home/admin/gta_scripts && '
                                                                     './sutas_container_build.sh ' '{{dag_run.conf['
                                                                     '"ref_path"]}} {{dag_run.conf["imagename"]}}',
                                run_as_user='admin')

    # Task 9 Gives status  Docker build docker_build_status=BashOperator(task_id='docker_build_status',
    # bash_command='pushd /home/admin/gta_scripts && python db_status_doc.py -i ' '{{dag_run.conf["user_id"]}} {{
    # dag_run.conf["state_doc"]}} {{dag_run.conf["status_doc"]}}')

    docker_build_status = PythonOperator(task_id='docker_build_status', provide_context=True,
                                         python_callable=write_db_doc)

    # Task 10 docker run
    # Task 10 docker run
    docker_run = BashOperator(task_id='docker_run',
                              bash_command='pushd /home/admin/gta_scripts && ./run_check_container.sh ' '{{dag_run'
                                           '.conf["containername"]}} {{dag_run.conf["imagename"]}}')

    # Task 11 Gives status docker run docker_run_status=BashOperator(task_id='docker_run_status',bash_command='pushd
    # /home/admin/gta_scripts && python db_status_run.py -i ' '{{dag_run.conf["user_id"]}} {{dag_run.conf[
    # "state_run"]}} {{dag_run.conf["status_run"]}}')

    docker_run_status = PythonOperator(task_id='docker_run_status', provide_context=True, python_callable=write_db_run)

    # Task 12 list out the test files
    list_out_tests = PythonOperator(task_id='list_out_tests', provide_context=True, python_callable=list_out_files)

    dummy_task >> bash_dir >> bash_git >> git_status >> ping_ser >> docker_params_update >> docker_build >> docker_build_status >> docker_run >> docker_run_status >> list_out_tests
