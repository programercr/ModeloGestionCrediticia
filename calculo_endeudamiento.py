import informe_ingresos
import deudas_clientes

class AnalisisEndeudamiento:
    def __init__(self):
        self.total_ingresos = 0
        self.total_deudas = 0

    def calcular_total_ingresos(self):
        calculadora_salarios = informe_ingresos.CalculadoraSalarios()
        calculadora_salarios.ingresar_salarios()
        self.total_ingresos = calculadora_salarios.calcular_promedio()

    def calcular_total_deudas(self):
        deudas = deudas_clientes()                
        deudas.clasificacion_deudas()

    def calcular_nivel_endeudamiento(self):
        if self.total_ingresos == 0:
            print("No se puede calcular el nivel de endeudamiento porque el total de ingresos es cero.")
            return
        nivel_endeudamiento = self.total_deudas / self.total_ingresos
        return nivel_endeudamiento

if __name__ == "__main__":
    analisis = AnalisisEndeudamiento()
    analisis.calcular_total_ingresos()
    analisis.calcular_total_deudas()
    nivel_endeudamiento = analisis.calcular_nivel_endeudamiento()
    if nivel_endeudamiento is not None:
        print(f'Nivel de endeudamiento: {nivel_endeudamiento:.2f}')
