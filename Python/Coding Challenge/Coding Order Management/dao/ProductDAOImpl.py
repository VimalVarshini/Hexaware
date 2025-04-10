from util.DB_Connect import db_connection

class ProductDAOImpl:
    def insert_product(self, product):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Products (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (product.product_id, product.product_name, product.description, product.price, product.quantity_in_stock, product.type))
        conn.commit()
        conn.close()

    def get_product_by_id(self, product_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Products WHERE productId = ?"
        cursor.execute(query, (product_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def update_product(self, product):
        conn = db_connection()
        cursor = conn.cursor()
        query = "UPDATE Products SET productName = ?, description = ?, price = ?, quantityInStock = ?, type = ? WHERE productId = ?"
        cursor.execute(query, (product.product_name, product.description, product.price, product.quantity_in_stock, product.type, product.product_id))
        conn.commit()
        conn.close()

    def delete_product(self, product_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Products WHERE productId = ?"
        cursor.execute(query, (product_id,))
        conn.commit()
        conn.close()

    def get_all_products(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return rows
