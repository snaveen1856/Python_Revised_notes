"""
from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime


args = {
    'start_date': datetime(2020, 2, 25),
    'owner': 'airflow'
     }

dag = DAG('sample_confg', default_args=args, schedule_interval=None)


def run_this_func(ds, **kwargs):
    print(f'''Remotely receive value of {kwargs["dag_run"].confg["message"] for_a_keys_of=message''')


    run_this = PythonOperator(
        task_id='run_this',
        provide_context=True,
        python_callable=run_this_func,
        dag=dag
    )

    # you can also accesss the Dag Run object in temples

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Here is the message :'
        {{dag_run.conf["message"] if dag_run else ""}}" ',
        dag = dag
        )

"""