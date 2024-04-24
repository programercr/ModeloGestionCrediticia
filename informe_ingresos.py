class CalculadoraSalarios:
    def __init__(self):
        self.salarios = []

    def ingresar_salarios(self):
        cantidad_salarios = int(input("Ingrese la cantidad de salarios a ingresar (entre 3 y 12): "))
        while cantidad_salarios < 3 or cantidad_salarios > 12:
            print("Debe ingresar entre 3 y 12 salarios.")
            cantidad_salarios = int(input("Ingrese la cantidad de salarios a ingresar (entre 3 y 12): "))

        for i in range(cantidad_salarios):
            salario = self.validar_input("Ingresar salario {}: ".format(i + 1))
            self.salarios.append(salario)

    def validar_input(self, mensaje):
        while True:
            try:
                salario = float(input(mensaje))
                if salario < 0:
                    print("El salario no puede ser negativo.")
                else:
                    return salario
            except ValueError:
                print("Ingrese un valor numérico válido.")

    def calcular_promedio(self):
        if not self.salarios:
            print("No se han ingresado salarios.")
            return

        promedio = sum(self.salarios) / len(self.salarios)
        return promedio

if __name__ == "__main__":
    calculadora = CalculadoraSalarios()
    calculadora.ingresar_salarios()
    promedio_salarios = calculadora.calcular_promedio()
    if promedio_salarios is not None:
        print("Salario Promedio:", promedio_salarios)

