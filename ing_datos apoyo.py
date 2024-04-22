import tipo_cliente as diego  
def informacion_usuario():
    documento_id = input("Ingrese el Documento de Identidad: ")
    nombre = input("Ingrese el Nombre: ")
    apellidos = input("Ingrese sus Apellidos: ")
    fecha_nacimiento = input("Ingrese la Fecha de Nacimiento (YYYY-MM-DD): ")
    estado_civil = input("Ingrese el Estado Civil: ")
    provincia = input("Ingresar Provincia: ")
    correo_electronico = input("Ingrese el Correo Electrónico: ")
    telefono = input("Ingrese Teléfono: ")

    return documento_id, nombre, apellidos, fecha_nacimiento, estado_civil, provincia, correo_electronico, telefono

# Uso de la función
#documento_id, nombre, apellidos, fecha_nacimiento, estado_civil, provincia, correo_electronico, telefono = informacion_usuario()
"""
# Luego puedes utilizar las variables retornadas según necesites
print("Documento de Identidad:", documento_id)
print("Nombre:", nombre)
print("Apellidos:", apellidos)
print("Fecha de Nacimiento:", fecha_nacimiento)
print("Estado Civil:", estado_civil)
print("Provincia:", provincia)
print("Correo Electrónico:", correo_electronico)
print("Teléfono:", telefono)"""

'''esta sintaxis me ayuda a jalar informacion de otro modulo
variable=diego.tipo_empleo()
print(f'Tipo de empleo seleccionado: {variable}')'''

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

    def ingresar_informacion(self):
        self.documento_id = input("Ingrese el Documento de Identidad: ")
        self.nombre = input("Ingrese el Nombre: ")
        self.apellidos = input("Ingrese sus Apellidos: ")
        self.fecha_nacimiento = input("Ingrese la Fecha de Nacimiento (YYYY-MM-DD): ")
        self.estado_civil = input("Ingrese el Estado Civil: ")
        self.provincia = input("Ingresar Provincia: ")
        self.correo_electronico = input("Ingrese el Correo Electrónico: ")
        self.telefono = input("Ingrese Teléfono: ")

    def obtener_informacion(self):
        return (self.documento_id, self.nombre, self.apellidos, self.fecha_nacimiento,
                self.estado_civil, self.provincia, self.correo_electronico, self.telefono)

# Ejemplo de uso:
usuario = Usuario()
usuario.ingresar_informacion()
informacion = usuario.obtener_informacion()
print("Información del usuario:", informacion)
