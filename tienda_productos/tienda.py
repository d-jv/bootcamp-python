from producto import Producto

class Tienda:
    def __init__(self, name) -> None:
        self.name = name
        self.productsList = []
    def add_product (self, new_product):
        self.productsList.append(new_product)
        return self
    def sell_product (self, id):
        # self.productsList = list(filter(lambda x:x != id, self.productsList)) # Falta llenar aqui
        self.productsList.pop(id)
        return self
    def inflation (self, percent_increase):
        for product in self.productsList:
            product.update_price(percent_increase, True)
        self
    def set_clearance (self, category, percent_discount):
        for product in self.productsList:
            if product.category == category:
                product.update_price(percent_discount, False)
    def vitrina(self):
        print('Productos en vitrina actualmente:')
        for product in self.productsList:
            print(f'- {product}')