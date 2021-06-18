from producto import Producto
from tienda import Tienda
import unittest
import random



class storeAndProductTests(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testAddStore(self):
        tienda999 = Tienda('Testing')
        esperado = 'Testing'
        self.assertEqual(tienda999.name, esperado)

    def testAddProduct(self):
        chocapic = Producto('Chocapic 350g', 2000, 'cereal', 42)
        self.assertTrue(chocapic)

    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()