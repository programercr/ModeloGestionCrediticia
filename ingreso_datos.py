
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

class Asalariado(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Asalariado"
        self.salario = 0
        self.empleador = ""
        self.puesto = ""
    

    def datos_asalariado(self):
        self.empleador = input("Ingrese su empleador: ")
        self.puesto = input("Ingrese su puesto: ")
        self.salario = float(input("Ingrese el salario: "))
        return (self.empleador,self.puesto,self.salario)
    

class Independiente(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Independiente"
        self.ingresos_mensuales = 0

    def ingresar_ingresos_mensuales(self):
        self.ingresos_mensuales = float(input("Ingrese los ingresos mensuales: "))
        return self.ingresos_mensuales

class Pensionado(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Pensionado"
        self.pension = 0

    def ingresar_pension(self):
        self.pension = float(input("Ingrese la pensión: "))
        return self.pension

if __name__=="__main__":

    # Ejemplo de uso: 
    asalariado = Asalariado()
    asalariado.ingresar_informacion()
    asalariado.ingresar_salario()
    informacion_asalariado = asalariado.obtener_informacion()
    print("Información del usuario asalariado:", informacion_asalariado)

    independiente = Independiente()
    independiente.ingresar_informacion()
    independiente.ingresar_ingresos_mensuales()
    informacion_independiente = independiente.obtener_informacion()
    print("Información del usuario independiente:", informacion_independiente)

    pensionado = Pensionado()
    pensionado.ingresar_informacion()
    pensionado.ingresar_pension()
    informacion_pensionado = pensionado.obtener_informacion()
    print("Información del usuario pensionado:", informacion_pensionado)
