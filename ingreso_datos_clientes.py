from datetime import datetime, timedelta
from informe_ingresos import *
from deudas_clientes import *
import tipo_cliente
from productos_crediticios import *
from base_datos_clientes import *
import re

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
        self.documento_id = self.validar_documento()
        self.nombre = self.validar_nombre()
        self.apellidos = self.validar_apellidos()
        self.fecha_nacimiento = self.validar_fecha_nacimiento()
        self.estado_civil = self.validar_estado_civil()
        self.provincia = self.validar_provincia()
        self.correo_electronico = self.validar_correo_electronico()
        self.telefono = self.validar_telefono()

    def validar_documento(self):
        base_de_datos = BaseDeDatosCSV("usuarios.csv")
        while True:
            documento = input("Ingrese el Documento de Identificación: ")
            if documento.isdigit() and len(documento) == 9:
                # Llamar a la función validar_usuario_en_dasedatos para verificar si el usuario existe
                usuario_existe = base_de_datos.validar_usuario_en_dasedatos(documento)
                if usuario_existe:
                    print("El usuario ya existe en la base de datos.\n")
                    tipo_cliente.tipo_empleo()
                else:
                    # Si el usuario no existe, se devuelve el documento
                    return documento
            else:
                print("Por favor, ingrese un documento de identificación válido con 9 dígitos.")


    def validar_nombre(self):
        while True:
            nombre = input("Ingrese el Nombre: ")
            if nombre.isalpha():
                return nombre
            else:
                print("El nombre solo puede contener letras.")

    def validar_apellidos(self):
        while True:
            apellidos = input("Ingrese sus Apellidos: ")
            if apellidos.replace(" ", "").isalpha():
                return apellidos
            else:
                print("Los apellidos solo pueden contener letras y espacios.")

    def validar_fecha_nacimiento(self):
        while True:
            fecha_nacimiento = input("Ingrese la Fecha de Nacimiento (YYYY-MM-DD): ")
            try:
                fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
                if datetime.now() - fecha_nacimiento < timedelta(days=365*18):
                    print("Debe ser mayor de 18 años para registrarse.")
                else:
                    return fecha_nacimiento.strftime("%Y-%m-%d")
            except ValueError:
                print("Por favor, ingrese una fecha válida en el formato especificado.")

    def validar_estado_civil(self):
        opciones_estado_civil = ["Soltero/a", "Casado/a", "Unión libre o unión de hecho",
                                 "Separado/a", "Divorciado/a", "Viudo/a"]
        while True:
            print("Seleccione su estado civil:")
            for i, opcion in enumerate(opciones_estado_civil, 1):
                print(f"{i}. {opcion}")
            opcion_estado_civil = input("Ingrese el número correspondiente a su estado civil: ")
            if opcion_estado_civil.isdigit() and 1 <= int(opcion_estado_civil) <= len(opciones_estado_civil):
                return opciones_estado_civil[int(opcion_estado_civil) - 1]
            else:
                print("Por favor, ingrese un número válido.")

    def validar_provincia(self):
        provincias_validas = ["cartago", "limon", "san jose", "heredia", "guanacaste", "alajuela", "puntarenas"]
        while True:
            provincia = input("Ingresar Provincia: ")
            if provincia.lower() in provincias_validas:
                return provincia
            else:
                print("Provincia inválida. Por favor, ingrese una provincia válida.")

    def validar_correo_electronico(self):
        while True:
            correo_electronico = input("Ingrese el Correo Electrónico: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", correo_electronico):
                return correo_electronico
            else:
                print("Por favor, ingrese un correo electrónico válido.")

    def validar_telefono(self):
        while True:
            telefono = input("Ingrese Teléfono: ")
            if telefono.isdigit() and len(telefono) == 8:
                return telefono
            else:
                print("Por favor, ingrese un número de teléfono válido con 8 dígitos.")

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
        self.sujeto_credito = 0

    def ingresar_informacion(self):
        super().ingresar_informacion()
        self.empleador = input("Ingrese su empleador: ")
        self.puesto = input("Ingrese su puesto: ")
        self.salario = self.validar_salario()
        self.antiguedadLaboral = tipo_cliente.antiguedad_laboral()
        print('Ahora calcularemos su promedio de Ingresos')
        ingresoscliente = CalculadoraIngresos()
        ingresoscliente.registrar_ingresos()
        promedio_ingresos = ingresoscliente.calcular_promedio()
        self.ingresos = promedio_ingresos
        print('Ahora registraremos sus deudas actuales')
        deudascliente = Deuda()
        self.deudas = deudascliente.clasificacion_deudas()
        self.nivel_Endeudamiento = self.deudas / self.ingresos
        print(f'Su nivel de endeudamiento es: {round((self.nivel_Endeudamiento * 100), 0)}%')

        if self.nivel_Endeudamiento <= 0.5:
            self.sujeto_credito = 1
            return self.documento_id,self.sujeto_credito
        else:
            return self.sujeto_credito
            
          

    def validar_salario(self):
        while True:
            try:
                salario = float(input("Ingrese el salario: $"))
                return salario
            except ValueError:
                print("Por favor, ingrese un salario válido.")

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

class Independiente(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Independiente"
        self.ingresos_mensuales = 0
        self.ingresos = 0
        self.deudas = 0
        self.sujeto_credito = 0

    def ingresar_informacion(self):
        super().ingresar_informacion()
        self.ingresos_mensuales = self.validar_ingresos_mensuales()
        print('Ahora calcularemos su promedio de Ingresos')
        ingresoscliente = CalculadoraIngresos()
        ingresoscliente.registrar_ingresos()
        promedio_ingresos = ingresoscliente.calcular_promedio()
        self.ingresos = promedio_ingresos
        print('Ahora registraremos sus deudas actuales')
        deudascliente = Deuda()
        self.deudas = deudascliente.clasificacion_deudas()
        self.nivel_Endeudamiento = self.deudas / self.ingresos
        print(f'Su nivel de endeudamiento es: {round((self.nivel_Endeudamiento * 100), 0)}%')

        if self.nivel_Endeudamiento <= 0.5:
            self.sujeto_credito = 1
            return self.documento_id,self.sujeto_credito
        else:
            return self.sujeto_credito
           

    def validar_ingresos_mensuales(self):
        while True:
            try:
                ingresos_mensuales = float(input("Digite sus ingresos mensuales: $"))
                return ingresos_mensuales
            except ValueError:
                print("Por favor, ingrese un monto válido.")

    def obtener_informacion(self):
        info_padre = super().obtener_informacion()
        return {
            **info_padre,
            "tipo_empleado": self.tipo_empleado,
            "ingresos_mensuales": self.ingresos_mensuales,
            "ingresos": self.ingresos,
            "deudas": self.deudas,
            "nivel_Endeudamiento": self.nivel_Endeudamiento
        }

class Pensionado(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo_empleado = "Pensionado"
        self.pension = 0
        self.sujeto_credito = 0

    def ingresar_informacion(self):
        super().ingresar_informacion()
        self.pension = self.validar_pension()
        print('Ahora registraremos sus deudas actuales')
        deudascliente = Deuda()
        self.deudas = deudascliente.clasificacion_deudas()
        self.nivel_Endeudamiento = self.deudas / self.pension
        print(f'Su nivel de endeudamiento es: {round((self.nivel_Endeudamiento * 100), 0)}%')

        if self.nivel_Endeudamiento <= 0.5:
            self.sujeto_credito = 1
            return self.documento_id, self.sujeto_credito
        else:
            return self.sujeto_credito
           

    def validar_pension(self):
        while True:
            try:
                pension = float(input("Ingrese monto de pensión: $"))
                return pension
            except ValueError:
                print("Por favor, ingrese un monto válido.")

    def obtener_informacion(self):
        info_padre = super().obtener_informacion()
        return {
            **info_padre,
            "pension": self.pension,
            "tipo_empleado": self.tipo_empleado,
            "deudas": self.deudas,
            "nivel_Endeudamiento": self.nivel_Endeudamiento
        }

if __name__ == "__main__":
    asalariado = Asalariado()
    asalariado.ingresar_informacion()
    print(asalariado.obtener_informacion())

    independiente = Independiente()
    independiente.ingresar_informacion()
    print(independiente.obtener_informacion())

    pensionado = Pensionado()
    pensionado.ingresar_informacion()
    print(pensionado.obtener_informacion())