from producto import Producto
from tienda import Tienda

tienda1 = Tienda('Tienda1')
chocapic = Producto('Chocapic 350g', 2000, 'cereal', 42)
colacaoMini = Producto('ColaCao Mini 400g', 2500, 'cereal', 35)
tienda1.add_product('te').add_product('cafe').vitrina()
chocapic.print_info()
tienda1.add_product('chicha').vitrina()
tienda1.sell_product(0).vitrina()