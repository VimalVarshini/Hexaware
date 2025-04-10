from util.DB_Connect import db_connection
from entity.Transaction import Transaction

class TransactionDAOImpl:
    def insert_transaction(self, transaction):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Transactions (account_id, transaction_type, amount, transaction_date, description) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (transaction.account_id, transaction.transaction_type, transaction.amount, transaction.date, transaction.description))
        conn.commit()
        conn.close()

    def get_transactions_by_account(self, account_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Transactions WHERE account_id = ?", (account_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_transactions_by_date_range(self, account_id, from_date, to_date):
        conn = db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Transactions WHERE account_id = ? AND transaction_date BETWEEN ? AND ?"
        cursor.execute(query, (account_id, from_date, to_date))
        rows = cursor.fetchall()
        conn.close()
        return rows
