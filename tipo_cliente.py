from ingreso_datos import *

def tipo_empleo():
    print("Seleccione el tipo de empleo:")
    print("1. Asalariado")
    print("2. Independiente")
    print("3. Pensionado")

    opcion = int(input("Ingrese el número correspondiente al tipo de empleado: "))

    if opcion == 1:        
        asalariado = Asalariado ()
        asalariado.ingresar_informacion()
        antiguedad = antiguedad_laboral()
        asalariado.obtener_informacion()
        info_usuario = asalariado.obtener_informacion()
        print("Información del usuario:", info_usuario,antiguedad)
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
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        return tipo_empleo()


def antiguedad_laboral():
    print("Seleccione su antigüedad laboral:")
    print("1. 0 - 3 meses")
    print("2. 3 - 6 meses")
    print("3. 6 - 12 meses")
    print("4. Mayor a 12 meses")

    opcion = int(input("Ingrese el número correspondiente a su opción: "))

    if opcion == 1:
        return "0 - 3 meses"
    elif opcion == 2:
        return "3 - 6 meses"
    elif opcion == 3:
        return "6 - 12 meses"
    elif opcion == 4:
        return "Mayor a 12 meses"
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        return antiguedad_laboral()

if __name__=="__main__":
    tipo_empleo ()