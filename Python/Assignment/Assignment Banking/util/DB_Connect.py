import pyodbc

def db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=VARSHINI;'
            'DATABASE=Banking;'
            'Trusted_Connection=yes;'
        )
        print("✅ Database connection established.")
        return conn
    except pyodbc.Error as e:
        print("❌ Error connecting to database:", e)