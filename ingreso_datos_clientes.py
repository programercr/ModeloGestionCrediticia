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
        self.documento_id = input("Ingrese el Documento de Identificación: ")
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


class Asalariado(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Asalariado"
        self.salario = 0
        self.empleador = ""
        self.puesto = ""

    def ingresar_informacion(self):
        super().ingresar_informacion()
        self.empleador = input("Ingrese su empleador: ")
        self.puesto = input("Ingrese su puesto: ")
        while True:
            try:
                self.salario = float(input("Ingrese el salario: "))
                break
            except ValueError:
                print("Por favor, ingrese un salario válido.")

    def obtener_informacion(self):
        info_padre = super().obtener_informacion()
        return info_padre + (self.empleador, self.puesto, self.salario, self.tipo_empleado)


class Independiente(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Independiente"
        self.ingresos_mensuales = 0

    def ingresar_informacion(self):
        super().ingresar_informacion()
        while True:
            try:
                self.ingresos_mensuales = float(input("Ingrese los ingresos mensuales: "))
                break
            except ValueError:
                print("Por favor, ingrese un monto válido.")

    def obtener_informacion(self):
        info_padre = super().obtener_informacion()
        return info_padre + (self.ingresos_mensuales, self.tipo_empleado)


class Pensionado(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Pensionado"
        self.pension = 0

    def ingresar_informacion(self):
        super().ingresar_informacion()
        while True:
            try:
                self.pension = float(input("Ingrese la pensión: "))
                break
            except ValueError:
                print("Por favor, ingrese un monto válido.")

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
    