import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma_enteros(self):
        resultado = suma(3, 5)
        self.assertEqual(resultado, 8)

    def test_suma_negativos(self):
        resultado = suma(-10, -7)
        self.assertEqual(resultado, -17)

    def test_suma_entero_y_decimal(self):
        resultado = suma(4, 3.5)
        self.assertEqual(resultado, 7.5)

    def test_suma_decimales(self):
        resultado = suma(2.5, 1.5)
        self.assertEqual(resultado, 4.0)

if __name__ == '__main__':
    unittest.main()
