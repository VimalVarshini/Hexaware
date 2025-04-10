from util.DB_Connect import db_connection

class ElectronicsDAOImpl:
    def insert_electronics(self, electronics):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Electronics (productId, brand, warrantyPeriod) VALUES (?, ?, ?)"
        cursor.execute(query, (electronics.product_id, electronics.brand, electronics.warranty_period))
        conn.commit()
        conn.close()

    def get_electronics_by_id(self, product_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Electronics WHERE productId = ?"
        cursor.execute(query, (product_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def update_electronics(self, electronics):
        conn = db_connection()
        cursor = conn.cursor()
        query = "UPDATE Electronics SET brand = ?, warrantyPeriod = ? WHERE productId = ?"
        cursor.execute(query, (electronics.brand, electronics.warranty_period, electronics.product_id))
        conn.commit()
        conn.close()

    def delete_electronics(self, product_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Electronics WHERE productId = ?"
        cursor.execute(query, (product_id,))
        conn.commit()
        conn.close()

    def get_all_electronics(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Electronics")
        rows = cursor.fetchall()
        conn.close()
        return rows
