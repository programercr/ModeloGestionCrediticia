from datetime import datetime

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

    def ingresar_documento_id(self):
        while True:
            documento_id = input("Ingrese el Documento de Identificación: ")
            if documento_id.isdigit() and len(documento_id) == 9:
                self.documento_id = documento_id
                break
            else:
                print("Por favor, ingrese un documento de identificación válido con 9 dígitos.")

    def ingresar_nombre(self):
        nombre = input("Ingrese el Nombre: ")
        while not nombre.isalpha():
            print("El nombre solo puede contener letras.")
            nombre = input("Ingrese el Nombre: ")
        self.nombre = nombre

    def ingresar_apellidos(self):
        apellidos = input("Ingrese sus Apellidos: ")
        while not apellidos.replace(" ", "").isalnum():
            print("Los apellidos solo pueden contener caracteres alfanuméricos y espacios.")
            apellidos = input("Ingrese sus Apellidos: ")
        self.apellidos = apellidos

    def ingresar_fecha_nacimiento(self):
        while True:
            fecha_nacimiento = input("Ingrese la Fecha de Nacimiento (YYYY-MM-DD): ")
            try:
                fecha = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
                if 1924 <= fecha.year <= 2006 and 1 <= fecha.month <= 12 and 1 <= fecha.day <= 31:
                    self.fecha_nacimiento = fecha_nacimiento
                    if fecha.year > 2006:
                        print("Menor de edad no sujeto a crédito.")
                    break
                else:
                    print("Ingrese una fecha válida (YYYY-MM-DD) dentro del rango permitido.")
            except ValueError:
                print("Por favor, ingrese una fecha en el formato correcto (YYYY-MM-DD).")

    def ingresar_estado_civil(self):
        self.estado_civil = input("Ingrese el Estado Civil: ")

    def ingresar_provincia(self):
        provincias_validas = ["cartago", "limon", "san jose", "heredia", "guanacaste", "alajuela", "puntarenas"]
        while True:
            provincia = input("Ingresar Provincia: ").lower()
            if provincia in provincias_validas:
                self.provincia = provincia
                break
            else:
                print("Provincia inválida. Por favor, ingrese una provincia válida.")

    def ingresar_correo_electronico(self):
        self.correo_electronico = input("Ingrese el Correo Electrónico: ")

    def ingresar_telefono(self):
        while True:
            telefono = input("Ingrese Teléfono: ")
            if telefono.isdigit() and len(telefono) == 8:
                self.telefono = telefono
                break
            else:
                print("Por favor, ingrese un número de teléfono válido con 8 dígitos.")

    def obtener_informacion(self):
        return (self.documento_id, self.nombre, self.apellidos, self.fecha_nacimiento,
                self.estado_civil, self.provincia, self.correo_electronico, self.telefono)


class Empleado(Usuario):
    def __init__(self, tipo_empleado):
        super().__init__()
        self.tipo_empleado = tipo_empleado
        self.salario = 0
        self.empleador = ""
        self.puesto = ""

    def ingresar_empleador(self):
        self.empleador = input("Ingrese su empleador: ")

    def ingresar_puesto(self):
        self.puesto = input("Ingrese su puesto: ")

    def ingresar_salario(self):
        while True:
            try:
                self.salario = float(input("Ingrese el salario: "))
                break
            except ValueError:
                print("Por favor, ingrese un salario válido.")

    def obtener_informacion(self):
        info_padre = super().obtener_informacion()
        return info_padre + (self.empleador, self.puesto, self.salario, self.tipo_empleado)


class Asalariado(Empleado):
    def __init__(self):
        super().__init__("Asalariado")

    def ingresar_informacion(self):
        super().ingresar_documento_id()
        super().ingresar_nombre()
        super().ingresar_apellidos()
        super().ingresar_fecha_nacimiento()
        super().ingresar_estado_civil()
        super().ingresar_provincia()
        super().ingresar_correo_electronico()
        super().ingresar_telefono()
        super().ingresar_empleador()
        super().ingresar_puesto()
        super().ingresar_salario()


class Independiente(Empleado):
    def __init__(self):
        super().__init__("Independiente")

    def ingresar_informacion(self):
        super().ingresar_documento_id()
        super().ingresar_nombre()
        super().ingresar_apellidos()
        super().ingresar_fecha_nacimiento()
        super().ingresar_estado_civil()
        super().ingresar_provincia()
        super().ingresar_correo_electronico()
        super().ingresar_telefono()
        super().ingresar_salario()


class Pensionado(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Pensionado"
        self.pension = 0

    def ingresar_pension(self):
        while True:
            try:
                self.pension = float(input("Ingrese monto de pensión: "))
                break
            except ValueError:
                print("Por favor, ingrese un monto válido.")

    def ingresar_informacion(self):
        super().ingresar_documento_id()
        super().ingresar_nombre()
        super().ingresar_apellidos()
        super().ingresar_fecha_nacimiento()
        super().ingresar_estado_civil()
        super().ingresar_provincia()
        super().ingresar_correo_electronico()
        super().ingresar_telefono()
        self.ingresar_pension()

    def obtener_informacion(self):
        info_padre = super().obtener_informacion()
        return info_padre + (self.pension, self.tipo_empleado)


if __name__ == "__main__":
    # Ejemplo de uso
    asalariado = Asalariado()
    asalariado.ingresar_informacion()
    print(asalariado.obtener_informacion())

    independiente = Independiente()
    independiente.ingresar_informacion()
    print(independiente.obtener_informacion())

    pensionado = Pensionado()
    pensionado.ingresar_informacion()
    print(pensionado.obtener_informacion())
