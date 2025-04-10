from entity.Products import Products

class Clothing(Products):
    def __init__(self, product_id, product_name, description, price, quantity_in_stock, size, color):
        super().__init__(product_id, product_name, description, price, quantity_in_stock, "Clothing")
        self.size = size
        self.color = color