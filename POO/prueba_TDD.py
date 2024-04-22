import unittest

def pedir_datos_personales():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    return nombre, apellido, edad

class TestPedirDatosPersonales(unittest.TestCase):
    def test_pedir_datos_personales(self):
        # Simulamos la entrada del usuario para las pruebas
        user_input = ['Pedro', 'Fernandez', '42']

        # Redefinimos la función input para que devuelva los valores simulados
        def mock_input(prompt):
            return user_input.pop(0)

        # Guardamos la función original de input y establecemos el mock
        original_input = __builtins__.input
        __builtins__.input = mock_input

        # Ejecutamos la función que estamos probando
        nombre, apellido, edad = pedir_datos_personales()

        # Restauramos la función original de input
        __builtins__.input = original_input

        # Verificamos que los valores devueltos sean los esperados
        self.assertEqual(nombre, 'Pedro')
        self.assertEqual(apellido, 'Fernandez')
        self.assertEqual(edad, 42)

if __name__ == '__main__':
    unittest.main()
