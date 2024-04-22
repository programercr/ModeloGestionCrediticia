import unittest
from faker import Faker
from ingresaDatos import pedir_datos_persona

fake = Faker()

def pedir_datos_persona():
    nombre = fake.first_name()
    print(f'Nombre generado por Faker: {nombre}')
    apellido = fake.last_name()
    print(f'Apellido generado por Faker: {apellido}')
    edad = fake.random_int(min=18, max=90)
    print(f'Edad generada por Faker: {edad}')
    return nombre, apellido, edad

class TestPedirDatosPersona(unittest.TestCase):
    def test_pedir_datos_persona(self):
        nombre, apellido, edad = pedir_datos_persona()
        self.assertIsInstance(nombre, str)
        self.assertIsInstance(apellido, str)
        self.assertIsInstance(edad, int)
        self.assertGreaterEqual(edad, 18)
        self.assertLessEqual(edad, 90)

if __name__ == "__main__":
    unittest.main()
