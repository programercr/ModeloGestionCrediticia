import unittest
from unittest.mock import patch
from io import StringIO
from ferreteriaPoo import Persona, Registro, Cliente, Producto, main

class TestPersona(unittest.TestCase):
    def test_creacion_persona(self):
        # Creamos una instancia de Persona
        persona = Persona("1234567890", "Juan", "Perez", "30", "Colombiano", "Masculino")
        
        # Verificamos que los atributos se asignen correctamente
        self.assertEqual(persona.documento, "1234567890")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellidos, "Perez")
        self.assertEqual(persona.edad, "30")
        self.assertEqual(persona.nacionalidad, "Colombiano")
        self.assertEqual(persona.genero, "Masculino")

class TestCliente(unittest.TestCase):
    def test_creacion_cliente(self):
        # Creamos una instancia de Cliente con datos de ejemplo diferentes
        cliente = Cliente("9876543210", "María", "López", "25", "Mexicana", "Femenino")
        
        # Verificamos que los atributos se asignen correctamente (heredados de Persona)
        self.assertEqual(cliente.documento, "9876543210")
        self.assertEqual(cliente.nombre, "María")
        self.assertEqual(cliente.apellidos, "López")
        self.assertEqual(cliente.edad, "25")
        self.assertEqual(cliente.nacionalidad, "Mexicana")
        self.assertEqual(cliente.genero, "Femenino")


class TestProducto(unittest.TestCase):
    def test_creacion_producto(self):
        # Creamos una instancia de Producto
        producto = Producto("Martillo", 10.0)
        
        # Verificamos que los atributos se asignen correctamente
        self.assertEqual(producto.nombre_producto, "Martillo")
        self.assertEqual(producto.valor_unitario, 10.0)


class TestRegistro(unittest.TestCase):
    def setUp(self):
        self.registro = Registro()

    def test_agregar_cliente(self):
        cliente = Cliente("1234567890", "Juan", "Perez", "30", "Colombiana", "Masculino")
        self.registro.agregar_cliente(cliente)
        self.assertTrue(self.registro.cliente_registrado("1234567890"))

    def test_agregar_producto(self):
        cliente = Cliente("1234567890", "Juan", "Perez", "30", "Colombiana", "Masculino")
        producto = Producto("Martillo", 10.0)
        self.registro.agregar_cliente(cliente)
        self.registro.agregar_producto("1234567890", producto, 2, 20.0)
        productos = self.registro.listar_productos()
        self.assertIn("Martillo", productos)

    def test_cliente_registrado(self):
        cliente = Cliente("1234567890", "Juan", "Perez", "30", "Colombiana", "Masculino")
        self.registro.agregar_cliente(cliente)
        self.assertTrue(self.registro.cliente_registrado("1234567890"))

class TestMainFunction(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['6'])  # Simulamos que el usuario ingresa '6' para salir del programa
    def test_main_exit(self, mock_input, mock_stdout):
        main()  # Llamamos a la función main()
        output = mock_stdout.getvalue()  # Obtenemos la salida generada por la función main()
        self.assertIn("Saliendo del programa.", output)  # Verificamos que el mensaje de salida sea el esperado

if __name__ == '__main__':
    unittest.main()



