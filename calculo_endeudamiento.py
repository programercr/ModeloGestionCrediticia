import informe_ingresos 
import deudas_clientes

#nivel_endeudamiento (total_deudas)/(ingreso_promedio_mensual)

salario1 = float(input("Ingresar Salario 1: "))
salario2 = float(input("Ingresar Salario 2: "))
salario3 = float(input("Ingresar Salario 3: "))
salario_promedio= informe_ingresos.ingreso_promedio(salario1, salario2, salario3)
deudas=deudas_clientes.ingresar_deudas_crediticias()
nivel_endeudamiento=deudas/salario_promedio
print(f'calculo de endeudamiento: {round(nivel_endeudamiento,2)}')
