import informe_ingresos
import deudas_clientes


# Crear una instancia de la clase CalculadoraSalarios
calculadora_salarios = informe_ingresos.CalculadoraSalarios()

# Ingresar los salarios
calculadora_salarios.ingresar_salarios()

# Calcular el salario promedio
salario_promedio = calculadora_salarios.calcular_promedio()

# Guardar el salario promedio en una variable
total_ingresos = salario_promedio

print(f'Calculo salario es: {total_ingresos}')


# Crear instancias de las clases DeudaBancaria, DeudaFinanciera y DeudaAlmacenes
deuda_bancos = deudas_clientes.DeudaBancaria()
deuda_financieras = deudas_clientes.DeudaFinanciera()
deuda_almacenes = deudas_clientes.DeudaAlmacenes()

# Ingresar las deudas para cada tipo
deuda_bancos.ingresar_deuda()
deuda_financieras.ingresar_deuda()
deuda_almacenes.ingresar_deuda()

# Obtener el total de las deudas sumando las deudas de cada tipo
total_deudas = (
    deuda_bancos.obtener_monto()
    + deuda_financieras.obtener_monto()
    + deuda_almacenes.obtener_monto()
)

# Mostrar el total de las deudas
print("Total deudas:", total_deudas)


# Calcular el nivel de endeudamiento
nivel_endeudamiento = total_deudas / total_ingresos

# Mostrar el nivel de endeudamiento
print(f'Nivel de endeudamiento: {nivel_endeudamiento:.2f}')
