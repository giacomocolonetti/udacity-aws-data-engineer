from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(
        self,
        redshift_conn_id="",
        table="",
        sql_query="",
        *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.conn_id = redshift_conn_id
        self.table = table
        self.sql_query = sql_query
        

    def execute(self, context):
        self.log.info('Loading the Fact table')
        redshift = PostgresHook(postgres_conn_id=self.conn_id)
        redshift.run(f"INSERT INTO {self.table} {self.sql_query}")
