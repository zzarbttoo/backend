from sqlalchemy import create_engine
import os 
import pandas as pd

class SqlManager:
    def __init__(self):
        result_ops_db_url:str = os.getenv('DB_URL') 
        self.sql_engine = create_engine(result_ops_db_url)

    def execute_query(self, query:str):
        result = pd.read_sql_query(query, con=self.sql_engine)
        print(result)

    def insert_data(self, table_name, data_set):
        data_frame:pd.DataFrame = pd.DataFrame([data_set])
        result = data_frame.to_sql(table_name, self.sql_engine, index=False, schema='public', if_exists='append', method='multi')
        print(result)

    def sql_engin_close(self):
        self.sql_engine.dispose()
