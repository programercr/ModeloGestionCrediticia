import os
import csv
import pandas as pd

class BaseDeDatosCSV:
    def __init__(self, filename):
        self.filename = filename

        # Verificar si el archivo existe, si no, crearlo con los nombres de columna
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                column_names = [
                    "documento_id", "nombre", "apellidos", "fecha_nacimiento",
                    "estado_civil", "provincia", "correo_electronico", "telefono",
                    "tipo_empleado", "salario", "ingresos_mensuales", "pension", 
                    "empleador", "puesto", "antiguedadLaboral", "ingresos", 
                    "deudas", "nivel_Endeudamiento"
                ]
                writer.writerow(column_names)

    def guardar_usuario(self, usuario):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.obtener_nombres_columnas())
            writer.writerow(usuario.obtener_informacion())

    def validar_usuario_en_dasedatos(self, documento_id):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['documento_id'] == documento_id:
                    return True
        return False

    def obtener_nombres_columnas(self):
        return [
            "documento_id", "nombre", "apellidos", "fecha_nacimiento",
            "estado_civil", "provincia", "correo_electronico", "telefono",
            "tipo_empleado", "salario", "ingresos_mensuales", "pension", 
            "empleador", "puesto", "antiguedadLaboral", "ingresos", 
            "deudas", "nivel_Endeudamiento"
        ]


class LeerBaseDeDatos:
    def __init__(self, filename):
        self.filename = filename

    def leer_todos_los_usuarios(self):
        return pd.read_csv(self.filename)


if __name__ == "__main__":
    lector = LeerBaseDeDatos("usuarios.csv")
    df_usuarios = lector.leer_todos_los_usuarios()
    print(df_usuarios)

