from datetime import datetime, timedelta
from faker import Faker

class Usuario:
    def __init__(self):
        self.documento_id = ""
        self.nombre = ""
        self.apellidos = ""
        self.fecha_nacimiento = ""
        self.estado_civil = ""
        self.provincia = ""
        self.correo_electronico = ""
        self.telefono = ""

    def ingresar_informacion(self, documento_id, nombre, apellidos, fecha_nacimiento, estado_civil, provincia, correo_electronico, telefono):
        self.documento_id = documento_id
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.estado_civil = estado_civil
        self.provincia = provincia
        self.correo_electronico = correo_electronico
        self.telefono = telefono

    def obtener_informacion(self):
        return {
            "documento_id": self.documento_id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "fecha_nacimiento": self.fecha_nacimiento,
            "estado_civil": self.estado_civil,
            "provincia": self.provincia,
            "correo_electronico": self.correo_electronico,
            "telefono": self.telefono
        }

class Asalariado(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Asalariado"
        self.salario = 0
        self.empleador = ""
        self.puesto = ""
        self.ingresos = 0
        self.deudas = 0
        self.antiguedadLaboral = ''
        self.nivel_Endeudamiento = 0

    def ingresar_informacion(self, documento_id, nombre, apellidos, fecha_nacimiento, estado_civil, provincia, correo_electronico, telefono, empleador, puesto, salario):
        super().ingresar_informacion(documento_id, nombre, apellidos, fecha_nacimiento, estado_civil, provincia, correo_electronico, telefono)
        self.empleador = empleador
        self.puesto = puesto
        self.salario = salario

    def obtener_informacion(self):
        info_padre = super().obtener_informacion()
        return {
            **info_padre,
            "empleador": self.empleador,
            "puesto": self.puesto,
            "salario": self.salario,
            "tipo_empleado": self.tipo_empleado,
            "antiguedadLaboral": self.antiguedadLaboral,
            "ingresos": self.ingresos,
            "deudas": self.deudas,
            "nivel_Endeudamiento": self.nivel_Endeudamiento
        }

fake = Faker('es_ES')

if __name__ == "__main__":
    asalariado = Asalariado()
    asalariado.ingresar_informacion(
        documento_id=fake.random_number(digits=9),
        nombre=fake.first_name(),
        apellidos=fake.last_name(),
        fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
        estado_civil=fake.random_element(elements=("Soltero/a", "Casado/a", "Unión libre o unión de hecho", "Separado/a", "Divorciado/a", "Viudo/a")),
        provincia=fake.random_element(elements=("cartago", "limon", "san jose", "heredia", "guanacaste", "alajuela", "puntarenas")),
        correo_electronico=fake.email(),
        telefono=fake.random_number(digits=8),
        empleador=fake.company(),
        puesto=fake.job(),
        salario=fake.random_number(digits=6)
    )
    print(asalariado.obtener_informacion())
