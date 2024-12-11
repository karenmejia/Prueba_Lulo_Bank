import sqlite3
import pandas as pd
 
class Helper:
    
    def __init__(self, df, path):
        self.conn = sqlite3.connect(path + "/January_series.db")
        self.cursor = self.conn.cursor()
        self.df = df

    def create_table(self, table_name, fields):
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({fields})')
        print(f'Tabla "{table_name}" creada correctamente')

    def data_insert(self, table_name, fields):
        for _, row in self.df.iterrows():
            values = tuple(row)
            self.cursor.execute(f"INSERT INTO {table_name} {fields} VALUES {values}")
            self.cursor.fetchall()
            self.conn.commit()
    
    def read(self, table_name):
        query_data = f"SELECT * FROM {table_name} LIMIT 5;"
        return pd.read_sql_query(query_data, self.conn)

    
 
