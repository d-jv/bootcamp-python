class Producto:
    def __init__(self, name, price, category, id) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.id = id
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price * (percent_change+1)
        else:
            self.price = self.price * (1-percent_change)
        return self
    def print_info(self):
        print(f'Nombre del producto: {self.name}\nCategoría: {self.category}\nPrecio: {self.price}')
        return self