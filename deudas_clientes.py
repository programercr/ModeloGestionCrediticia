def ingresar_deudas_crediticias():
    print("Por favor, ingrese sus deudas mensuales de operaciones crediticias:")

    deuda_mensual = float(input("Deudas mensuales de operaciones crediticias: "))

    return deuda_mensual

if __name__=="__main__":
    # Uso de la función
    deuda_mensual = ingresar_deudas_crediticias()
    print("Deuda mensual de operaciones crediticias:", deuda_mensual, )

