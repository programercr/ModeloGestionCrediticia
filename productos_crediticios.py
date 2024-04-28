import pandas as pd
from base_datos_clientes import LeerBaseDeDatos

class AnalizadorDeUsuarios:
    def __init__(self, filename):
        lector = LeerBaseDeDatos(filename)
        self.df_usuarios = lector.leer_todos_los_usuarios()
        self.df_usuarios['documento_id'] = self.df_usuarios['documento_id'].astype(str)
        self.productos_df = pd.DataFrame({
            'Años': [5, 6, 7, 8, 9, 10],
            'Meses': [60, 72, 84, 96, 108, 120]
        })

    def mostrar_datos(self):
        print(self.df_usuarios)

    def calcular_cuota(self, row):
        if row['tipo_empleado'] == 'Pensionado':
            return (row['pension'] - row['deudas'])*0.32
        else:
            return (row['ingresos'] - row['deudas']) * 0.32

    def agregar_cuota(self):
        self.df_usuarios['Cuota'] = self.df_usuarios.apply(self.calcular_cuota, axis=1)
        return self.df_usuarios

    def productos(self, documento_id):
        usuario = self.df_usuarios[self.df_usuarios['documento_id'] == documento_id]
        if not usuario.empty:
            cuota = usuario.iloc[0]['Cuota']
            tipo_empleado = usuario.iloc[0]['tipo_empleado']
            self.productos_df['Monto'] = self.productos_df['Meses'] * cuota
            columnas_tipo = {'Asalariado': 0.75, 'Independiente': 0.55, 'Pensionado': 0.40}
            for tipo, factor in columnas_tipo.items():
                self.productos_df[tipo] = self.productos_df['Monto'] * factor if tipo_empleado == tipo else 0

            # Filtrar solo la columna relevante para el tipo de empleado actual
            columnas_relevantes = ['Años', 'Meses', 'Monto', tipo_empleado]
            self.productos_df = self.productos_df[columnas_relevantes]

        return usuario, self.productos_df
    
    def elegir_producto(self):
        pass
    
if __name__ == "__main__":
    analizador = AnalizadorDeUsuarios("usuarios.csv")
    analizador.agregar_cuota()
    analizador.mostrar_datos()
    documento_id = '258369147'
    info_usuario, info_productos = analizador.productos(documento_id)
    print("Información del Usuario:")
    print(info_usuario)
    print("\nInformación de Productos:")
    print(info_productos)
    producto_seleccionado = analizador.elegir_producto()

