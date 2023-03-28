import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy.engine import create_engine
connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=########;DATABASE=#######;Trusted_Connection=yes"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
conn = create_engine(connection_url)

sql_query = "SELECT * FROM SalesData"

sql_query_data = (sql_query,conn)
