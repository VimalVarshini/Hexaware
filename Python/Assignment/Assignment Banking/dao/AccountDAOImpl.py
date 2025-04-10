from util.DB_Connect import db_connection
from entity.Accounts import Account

class AccountDAOImpl:
    def insert_account(self, account):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Accounts (customer_id, account_type, balance) VALUES (?, ?, ?)"
        cursor.execute(query, (account.customer.customer_id, account.account_type, account.balance))
        conn.commit()
        conn.close()

    def get_account_by_id(self, account_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Accounts WHERE account_id = ?"
        cursor.execute(query, (account_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def update_balance(self, account_id, new_balance):
        conn = db_connection()
        cursor = conn.cursor()
        query = "UPDATE Accounts SET balance = ? WHERE account_id = ?"
        cursor.execute(query, (new_balance, account_id))
        conn.commit()
        conn.close()

    def get_all_accounts(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Accounts")
        rows = cursor.fetchall()
        conn.close()
        return rows
