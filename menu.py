import csv

class Persona:
    def __init__(self, documento, nombre, apellidos, edad, nacionalidad, genero):
        # Aquí asigno los valores que me dan a las propiedades de la persona.
        self.documento = documento
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.genero = genero

class Cliente(Persona):
    def __init__(self, documento, nombre, apellidos, edad, nacionalidad, genero):
        # Uso el constructor de la clase Persona para no repetir código.
        super().__init__(documento, nombre, apellidos, edad, nacionalidad, genero)

class Producto:
    def __init__(self, nombre_producto, valor_unitario):
        # Simplemente guardo el nombre y el valor del producto.
        self.nombre_producto = nombre_producto
        self.valor_unitario = valor_unitario

class Registro:
    archivo_clientes = 'clientes.csv'
    archivo_productos = 'productos.csv'

    def inicializar_archivos(self):
        # Me aseguro de que los archivos existan desde el principio.
        try:
            with open(self.archivo_clientes, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Documento", "Nombre", "Apellidos", "Edad", "Nacionalidad", "Género"])
        except FileExistsError:
            pass

        try:
            with open(self.archivo_productos, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Documento Cliente", "Nombre Producto", "Valor Unitario", "Total Producto", "Precio Total"])
        except FileExistsError:
            pass

    def agregar_cliente(self, cliente):
        # Aquí añado un cliente al archivo CSV.
        with open(self.archivo_clientes, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([cliente.documento, cliente.nombre, cliente.apellidos, cliente.edad, cliente.nacionalidad, cliente.genero])

    def agregar_producto(self, documento_cliente, producto, total_producto, precio_total):
        # Y aquí añado un producto vendido al archivo correspondiente.
        with open(self.archivo_productos, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([documento_cliente, producto.nombre_producto, producto.valor_unitario, total_producto, precio_total])

    def cliente_registrado(self, documento):
        # Chequeo si un cliente ya está en el archivo de clientes.
        try:
            with open(self.archivo_clientes, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if documento == row[0]:
                        return True
            return False
        except FileNotFoundError:
            return False

    def listar_clientes(self):
        # Aquí muestro todos los clientes que tengo registrados.
        print("Lista de clientes registrados:")
        try:
            with open(self.archivo_clientes, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Salto la línea de los encabezados.
                for row in reader:
                    print(f"Documento: {row[0]}, Nombre: {row[1]} {row[2]}, Edad: {row[3]}, Nacionalidad: {row[4]}, Género: {row[5]}")
        except FileNotFoundError:
            print("No se encontró el archivo de clientes.")

    def listar_productos(self):
        productos = []
        try:
            with open(self.archivo_productos, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Salto la línea de los encabezados.
                for row in reader:
                    productos.append(row[1])  # Agrego el nombre del producto a la lista
            return productos
        except FileNotFoundError:
            print("No se encontró el archivo de productos.")

def informacion_plataforma():
    print("\nInformación de la Plataforma:")
    print("Nombre de la Plataforma: Ferreteria DJL S.A")
    print("Fecha de Creación: Abril de 2024")
    print("Desarrolladores: Johnny Jimenez, Diego Ramirez y Luis Alvarez")
    print("Lenguaje de Programación: Python")
    print("Descripción: Esta plataforma facilita la gestión de clientes y ventas de productos.")

def main():
    registro = Registro()  # Creo una instancia de Registro.
    registro.inicializar_archivos()

    while True:
        # Muestro el menú de opciones.
        print("\nMenú:")
        print("1. Agregar nuevo cliente")
        print("2. Registrar compra de producto")
        print("3. Ver lista de clientes")
        print("4. Ver lista de productos")
        print("5. Acerca de")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            documento = input("Documento de identidad: ")
            if registro.cliente_registrado(documento):
                print("El cliente ya está registrado.")
            else:
                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                edad = input("Edad: ")
                nacionalidad = input("Nacionalidad: ")
                genero = input("Género (Femenino/Masculino): ")
                cliente = Cliente(documento, nombre, apellidos, edad, nacionalidad, genero)
                registro.agregar_cliente(cliente)
                print("Cliente agregado exitosamente.")

        elif opcion == '2':
            documento_cliente = input("Documento de identidad del cliente: ")
            if not registro.cliente_registrado(documento_cliente):
                print("El cliente no está registrado.")
            else:
                nombre_producto = input("Nombre del producto: ")
                valor_unitario = float(input("Valor unitario: "))
                total_producto = int(input("Total de producto comprado: "))
                precio_total = valor_unitario * total_producto
                producto = Producto(nombre_producto, valor_unitario)
                registro.agregar_producto(documento_cliente, producto, total_producto, precio_total)
                print("Venta del producto registrada exitosamente.")

        elif opcion == '3':
            # Llamo al método que lista todos los clientes.
            registro.listar_clientes()

        elif opcion == '4':
            # Y este hace lo propio con los productos.
            registro.listar_productos()

        elif opcion == '5':
            informacion_plataforma()

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
