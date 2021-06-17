from producto import Producto

class Tienda:
    def __init__(self, name) -> None:
        self.name = name
        self.productList = []
    def add_product (self, new_product):
        self.productList.append(new_product)
        return self
    def sell_product (self, id):
        self.productList.pop(id)
        return self
    def inflation (self, percent_increase):
        self.price = self.price * (percent_increase+1)
    def set_clearance (self, category, percent_discount):
        pass
    def vitrina(self):
        print('Productos en vitrina actualmente:')
        for product in self.productList:
            print(f'- {product}')