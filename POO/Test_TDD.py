import unittest

'''
TDD, o Desarrollo Guiado por Pruebas (Test-Driven Development) en español, 
es una metodología de desarrollo de software que se centra en escribir pruebas automatizadas antes de escribir el código de producción. 
El ciclo básico de TDD consta de tres pasos: escribir una prueba que falle, 
escribir el código mínimo necesario para que la prueba pase y luego refactorizar el código para mejorar su diseño sin cambiar su comportamiento.'''

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
