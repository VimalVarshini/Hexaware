from entity.Products import Products

class Electronics(Products):
    def __init__(self, product_id, product_name, description, price, quantity_in_stock, brand, warranty_period):
        super().__init__(product_id, product_name, description, price, quantity_in_stock, "Electronics")
        self.brand = brand
        self.warranty_period = warranty_period