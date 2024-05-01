import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from informe_ingresos import CalculadoraIngresos

class TestCalculadoraIngresos(unittest.TestCase):
    def test_registrar_ingresos(self):
        inputs = ["4", "1000", "si", "1200", "si", "1500", "si", "1800", "si"]
        with patch('builtins.input', side_effect=inputs):
            calculadora = CalculadoraIngresos()
            calculadora.registrar_ingresos()
            self.assertEqual(calculadora.salarios, [1000, 1200, 1500, 1800])

    def test_validar_input(self):
        inputs = ["1000", "si"]
        with patch('builtins.input', side_effect=inputs):
            calculadora = CalculadoraIngresos()
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                salario = calculadora.validar_input("Digite el ingreso: $ ")
                self.assertEqual(salario, 1000)

    def test_calcular_promedio(self):
        calculadora = CalculadoraIngresos()
        calculadora.salarios = [1000, 1200, 1500, 1800]
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            promedio = calculadora.calcular_promedio()
            self.assertEqual(promedio, 1375.0)

if __name__ == '__main__':
    unittest.main()
