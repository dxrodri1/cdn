from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
import os

#set proxy
# os.environ['']

proxy = 'http://localhost:1234'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy


# Define the DAG
dag = DAG(
    'dbx_connectivity_dag7',
    description='A simple databricks dag',
    schedule_interval=None,
    start_date=None,
    catchup=False
)
token=''

# Define the BashOperator task
hello_dbx_task = BashOperator(
    task_id='hello_dbx_task',
    bash_command=f'curl -X GET -H "Authorization: Bearer {token}" https://one-.cloud.databricks.com/api/2.1/unity-catalog/catalogs >/tmp/t.out;cat /tmp/t.out',
    dag=dag
)

# Define the task dependencies
hello_dbx_task
