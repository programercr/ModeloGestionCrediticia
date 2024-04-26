import tipo_cliente
from informe_ingresos import *


#print('Bienvenido a la plataforma de registo de clientes, favor seleccione una de nuestras opciones: ')
#tipo_cliente.tipo_empleo()

print('Favor registras los ingresos del cliente')
promedio_ingresos = CalculadoraIngresos()
promedio_ingresos.ingresar_salarios()
promedio_salarios = promedio_ingresos.calcular_promedio()
if promedio_salarios is not None:
    print("Salario Promedio:", promedio_salarios)
