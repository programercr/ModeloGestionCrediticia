from ingreso_datos_clientes import *

def tipo_empleo():
    
    print('Bienvenido')
    print('Iniciaremos el registro de cliente')
    print("Seleccione el tipo de empleo:")
    print("1. Asalariado")
    print("2. Independiente")
    print("3. Pensionado")

    while True:
        opcion = input("Ingrese el número correspondiente al tipo de empleado: ")
        if opcion.isdigit():  # Verifica si la entrada es un número
            opcion = int(opcion)
            if opcion in [1, 2, 3]:  # Verifica si la opción está en el rango válido
                break
        print("Opción inválida. Por favor, seleccione una opción válida.")

    if opcion == 1:        
        asalariado = Asalariado()
        asalariado.ingresar_informacion()      
        asalariado.obtener_informacion()
        info_usuario = asalariado.obtener_informacion()
        print("Información del usuario:", info_usuario)
    elif opcion == 2:
        independiente = Independiente()
        independiente.ingresar_informacion()        
        info_usuario = independiente.obtener_informacion()
        print("Información del usuario:", info_usuario)
    elif opcion == 3:
        pensionado = Pensionado()
        pensionado.ingresar_informacion()
        info_usuario = pensionado.obtener_informacion()
        print("Información del usuario:", info_usuario)

def antiguedad_laboral():
    print("Cuanto tiempo tiene de laborar para la compañia :")
    print("1. 0 - 3 meses")
    print("2. 3 - 6 meses")
    print("3. 6 - 12 meses")
    print("4. Mayor a 12 meses")

    while True:
        opcion = input("Ingrese el número correspondiente a su opción: ")
        if opcion.isdigit():  # Verifica si la entrada es un número
            opcion = int(opcion)
            if opcion in [1, 2, 3, 4]:  # Verifica si la opción está en el rango válido
                break
        print("Opción inválida. Por favor, seleccione una opción válida.")

    if opcion == 1:
        return "0 - 3 meses"
    elif opcion == 2:
        return "3 - 6 meses"
    elif opcion == 3:
        return "6 - 12 meses"
    elif opcion == 4:
        return "Mayor a 12 meses"

if __name__=="__main__":
    tipo_empleo()
