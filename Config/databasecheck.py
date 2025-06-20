import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

server = os.getenv("SERVER")
database = os.getenv("DATABASE")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

conn = pyodbc.connect(
    rf'DRIVER={{ODBC Driver 17 for SQL Server}};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    rf'UID={username};'
    rf'PWD={password};'
    rf'Trusted_Connection=no;'
)

cursor = conn.cursor()
cursor.execute("SELECT TOP 10 * FROM CAMA.PARCEL WHERE TAX_YEAR = 2026")
for row in cursor.fetchall():
    print(row)
conn.close()