class CalculadoraIngresos:
    def __init__(self):
        self.salarios = []

    def registrar_ingresos(self):
        while True:
            try:
                cantidad_salarios = int(input("Digite la cantidad de Ingresos a registrar (entre 3 y 12): "))
                if 3 <= cantidad_salarios <= 12:
                    break
                else:
                    print("Debe ingresar entre 3 y 12 Ingresos.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

        for i in range(cantidad_salarios):
            salario = self.validar_input("Digite el ingreso # {}: $ ".format(i + 1))
            self.salarios.append(salario)

    def validar_input(self, mensaje):
        while True:
            try:
                salario = float(input(mensaje))
                if salario < 0:
                    print("Error: El Ingreso no puede ser negativo.")
                else:
                    return salario
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

    def calcular_promedio(self):
        if not self.salarios:
            print("No se han registrado ingresos.")
            return

        promedio = sum(self.salarios) / len(self.salarios)
        return promedio

if __name__ == "__main__":
    calculadora = CalculadoraIngresos()
    calculadora.registrar_ingresos()
    promedio_salarios = calculadora.calcular_promedio()
    if promedio_salarios is not None:
        print("Ingreso Promedio:", promedio_salarios)


