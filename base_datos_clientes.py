import csv
import pandas as pd

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
    


class LeerBaseDeDatos:
    def __init__(self, filename):
        self.filename = filename

    def leer_todos_los_usuarios(self):
        """Lee todos los usuarios desde el archivo CSV usando Pandas y devuelve un DataFrame."""
        return pd.read_csv(self.filename)


if __name__ == "__main__":
    lector = LeerBaseDeDatos("usuarios.csv")
    df_usuarios = lector.leer_todos_los_usuarios()
    print(df_usuarios)
