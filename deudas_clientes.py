class Deuda:
    def __init__(self):
        self.monto = 0
        self.cantidad_deudas = 0

    def ingresar_deuda(self, tipo_deuda):
        while True:
            try:
                cantidad_deudas = int(input(f"¿Cuántas deudas {tipo_deuda} tienes?: "))
                if cantidad_deudas <= 0:
                    print("Por favor, ingresa un número válido mayor que cero.")
                else:
                    total_deuda = 0
                    for i in range(1, cantidad_deudas + 1):
                        while True:
                            try:
                                monto = float(input(f"Ingrese el monto de la deuda {tipo_deuda} #{i}: "))
                                if monto <= 0:
                                    print("Por favor, ingresa un monto válido mayor que cero.")
                                else:
                                    total_deuda += monto
                                    break
                            except ValueError:
                                print("Por favor, ingresa un monto válido.")
                    self.monto += total_deuda
                    self.cantidad_deudas += cantidad_deudas
                    break
            except ValueError:
                print("Por favor, ingresa un número válido.")


def obtener_respuesta(pregunta):
    while True:
        respuesta = input(pregunta).lower()
        if respuesta == "si" or respuesta == "no":
            return respuesta
        else:
            print("Por favor, ingresa 'si' o 'no'.")


if __name__ == "__main__":
    tiene_deudas = obtener_respuesta("¿Tienes deudas con otras entidades? (si/no): ")

    if tiene_deudas == "si":
        deuda = Deuda()

        tiene_bancarias = obtener_respuesta("¿Tienes deudas bancarias? (si/no): ")
        if tiene_bancarias == "si":
            deuda.ingresar_deuda("bancarias")

        tiene_financieras = obtener_respuesta("¿Tienes deudas financieras? (si/no): ")
        if tiene_financieras == "si":
            deuda.ingresar_deuda("financieras")

        tiene_almacenes = obtener_respuesta("¿Tienes deudas con almacenes? (si/no): ")
        if tiene_almacenes == "si":
            deuda.ingresar_deuda("con almacenes")

        total_general = deuda.monto

        if total_general > 0:
            print("El total general de tus deudas es:", total_general)
            print("La cantidad total de deudas es:", deuda.cantidad_deudas)
        else:
            print("No tienes deudas. El total de deudas es cero.")
    else:
        print("No tienes deudas. El total de deudas es cero.")
