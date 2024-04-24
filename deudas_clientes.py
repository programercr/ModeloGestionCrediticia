class Deuda:
    def __init__(self):
        self.monto = 0

    def ingresar_deuda(self):
        while True:
            try:
                monto = float(input("Ingrese el monto de la deuda: "))
                if monto < 0:
                    print("Por favor, ingrese un monto válido.")
                else:
                    self.monto = monto
                    break
            except ValueError:
                print("Por favor, ingrese un monto válido.")

    def obtener_monto(self):
        return self.monto


class DeudaBancaria(Deuda):
    def __init__(self):
        super().__init__()


class DeudaFinanciera(Deuda):
    def __init__(self):
        super().__init__()


class DeudaAlmacenes(Deuda):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    tiene_deudas = input("¿Tiene deudas? (si/no): ").lower() == "si"

    if tiene_deudas:
        deuda_bancos = DeudaBancaria()
        deuda_bancos.ingresar_deuda()

        deuda_financieras = DeudaFinanciera()
        deuda_financieras.ingresar_deuda()

        deuda_almacenes = DeudaAlmacenes()
        deuda_almacenes.ingresar_deuda()

        total_general = (
            deuda_bancos.obtener_monto()
            + deuda_financieras.obtener_monto()
            + deuda_almacenes.obtener_monto()
        )

        print("\nDeuda con otros bancos:", deuda_bancos.obtener_monto())
        print("Deuda con financieras:", deuda_financieras.obtener_monto())
        print("Deuda con almacenes:", deuda_almacenes.obtener_monto())
        print("Total general de deudas:", total_general)
    else:
        print("No tiene deudas. El total de deudas es cero.")


