import csv

class BaseDeDatosCSV:
    def __init__(self, filename):
        self.filename = filename

    def guardar_usuario(self, usuario):
        # Nombres de las columnas
        column_names =  [
            "documento_id", "nombre", "apellidos", "fecha_nacimiento",
            "estado_civil", "provincia", "correo_electronico", "telefono",
            "tipo_empleado", "salario", "ingresos_mensuales", "pension", 
            "empleador", "puesto", "antiguedadLaboral", "ingresos", 
            "deudas", "nivel_Endeudamiento"
        ]
        with open(self.filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=column_names)
            
            # Si el archivo está vacío, escribe los nombres de las columnas
            if file.tell() == 0:
                writer.writeheader()

            # Guarda los datos del usuario en el archivo
            writer.writerow(usuario.obtener_informacion())

    def validar_usuario_en_dasedatos(self, documento_id):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['documento_id'] == documento_id:
                    # El usuario ya existe
                    return True
        # Si no se encuentra ninguna coincidencia después de iterar sobre todas las filas
        return False


if __name__ == "__main__":
    # Crear una instancia de la base de datos
    base_de_datos = BaseDeDatosCSV("usuarios.csv")

    # Llamar al método validar_usuario y proporcionarle el documento_id a validar
    documento_id = '123456789'  # Este sería el documento_id que deseas validar
    resultado_validacion = base_de_datos.validar_usuario_en_dasedatos(documento_id)
