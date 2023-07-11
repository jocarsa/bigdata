import pandas as pd
import sqlite3

excel_file_path = 'empresas.xls'

df = pd.read_excel(excel_file_path)

database_file_path = 'empresas.db'

conn = sqlite3.connect(database_file_path)

df.to_sql('empresas', conn, index=False, if_exists='replace')

conn.commit()
conn.close()
