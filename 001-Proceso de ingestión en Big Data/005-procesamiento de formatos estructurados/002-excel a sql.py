import pandas as pd
import sqlite3

excel_file_path = 'basededatos.xlsx'

df = pd.read_excel(excel_file_path)

database_file_path = 'basededatos.db'

conn = sqlite3.connect(database_file_path)

df.to_sql('table_name', conn, index=False, if_exists='replace')

conn.commit()
conn.close()
