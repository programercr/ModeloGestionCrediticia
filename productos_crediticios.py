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
        print(self.df_usuarios.to_string(index=False))

    def calcular_cuota(self, row):
        if row['tipo_empleado'] == 'Pensionado':
            return (row['pension'] - row['deudas']) * 0.32
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

            # Crear la columna 'Monto' al principio del DataFrame
            self.productos_df['Monto'] = self.productos_df['Meses'] * cuota

            # Modificar el DataFrame según el tipo de empleado
            columnas_tipo = {'Asalariado': 0.75, 'Independiente': 0.55, 'Pensionado': 0.40}
            for tipo, factor in columnas_tipo.items():
                self.productos_df[tipo] = self.productos_df['Monto'] * factor if tipo_empleado == tipo else 0

            # Filtrar solo las columnas relevantes
            columnas_relevantes = ['Años', 'Meses', 'Monto', tipo_empleado]
            self.productos_df = self.productos_df[columnas_relevantes]

        return usuario, self.productos_df
        
    
    def elegir_producto(self):
        # Agregar la columna 'Opcion' como la primera columna
        productos_con_opcion = self.productos_df.copy()
        productos_con_opcion.insert(0, 'Opcion', range(1, len(productos_con_opcion) + 1))

        # Eliminar la columna 'Monto'
        productos_sin_monto = productos_con_opcion.drop(columns=['Monto'])

        # Renombrar las columnas
        productos_sin_monto.columns = ['Opcion', 'Años', 'Meses', 'Cantidad a financiar']

        print('\n',productos_sin_monto.to_string(index=False))

        # Pedir al usuario que elija una opción
        while True:
            try:
                opcion_elegida = int(input("\n¿Qué producto desea adquirir? Por favor, elija una opción: "))
                if opcion_elegida not in productos_sin_monto['Opcion'].values:
                    raise ValueError("Opción no válida. Por favor, elija una opción de la lista.")
                break
            except ValueError as e:
                print(e)

        # Filtrar el DataFrame según la opción elegida por el usuario
        producto_elegido = productos_sin_monto[productos_sin_monto['Opcion'] == opcion_elegida]

        return producto_elegido
    
    def usuario_producto(self, usuario_info, producto_info):
        # Mostrar la información del usuario
        print("\nInformación del Crédito:")
        print("Documento_id:", usuario_info.iloc[0]['documento_id'])
        print("Nombre:", usuario_info.iloc[0]['nombre'])
        print("Apellidos:", usuario_info.iloc[0]['apellidos'])
        print("Cuota:", usuario_info.iloc[0]['Cuota'])
        print("Años:", producto_info['Años'].values[0])
        print("Meses:", producto_info['Meses'].values[0])
        print("Cantidad a financiar:", producto_info['Cantidad a financiar'].values[0])

        # Retornar los datos del usuario y del producto
        return {
            'documento_id': usuario_info.iloc[0]['documento_id'],
            'cuota': usuario_info.iloc[0]['Cuota'],
            'años': producto_info['Años'].values[0],
            'meses': producto_info['Meses'].values[0],
            'cantidad_a_financiar': producto_info['Cantidad a financiar'].values[0]
        }


    
if __name__ == "__main__":
    analizador = AnalizadorDeUsuarios("usuarios.csv")
    analizador.agregar_cuota()
    documento_id = '123456789'
    info_usuario, info_productos = analizador.productos(documento_id)
    producto_seleccionado = analizador.elegir_producto()
    info_producto = analizador.usuario_producto(info_usuario, producto_seleccionado)


