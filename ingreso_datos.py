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
        self.documento_id = input("Ingrese el Documento de Identificacion: ")
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
        self.salario = float(input("Ingrese el salario: "))

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
        self.ingresos_mensuales = float(input("Ingrese los ingresos mensuales: "))

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
        self.pension = float(input("Ingrese la pensión: "))

    def obtener_informacion(self):
        info_padre = super().obtener_informacion()
        return info_padre + (self.pension, self.tipo_empleado)
    
    
if __name__ == "__main__":
    pass

