from util.DB_Connect import db_connection
from entity.Customer import Customer

class CustomerDAOImpl:
    def insert_customer(self, customer):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Customers (first_name, last_name, DOB, email, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (customer.first_name, customer.last_name, customer.DOB, customer.email, customer.phone_number, customer.address))
        conn.commit()
        conn.close()

    def get_customer_by_id(self, customer_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Customers WHERE customer_id = ?"
        cursor.execute(query, (customer_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def get_all_customers(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customers")
        rows = cursor.fetchall()
        conn.close()
        return rows
