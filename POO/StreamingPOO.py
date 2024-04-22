import csv
import os
import pandas as pd

class Tipo_Producto:
    def __init__(self, titulo, genero, fecha_publicacion):
        self.titulo = titulo
        self.genero = genero
        self.fecha_publicacion = fecha_publicacion
    
class Canciones(Tipo_Producto):
    def __init__(self, titulo, genero, fecha_publicacion, album, artista):
        super().__init__(titulo, genero, fecha_publicacion)
        self.album = album
        self.artista = artista

class Peliculas(Tipo_Producto):
    def __init__(self, titulo, genero, fecha_publicacion, director, actores):
        super().__init__(titulo, genero, fecha_publicacion)
        self.director = director
        self.actores = actores

def guardar_pelicula(pelicula):
    archivo_peliculas = 'peliculas.csv'
    columnas = ['titulo', 'genero', 'fecha_publicacion', 'director', 'actores']
    necesita_encabezado = not os.path.exists(archivo_peliculas)
    
    with open(archivo_peliculas, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columnas)
        if necesita_encabezado:
            writer.writeheader()
        writer.writerow({
            'titulo': pelicula.titulo,
            'genero': pelicula.genero,
            'fecha_publicacion': pelicula.fecha_publicacion,
            'director': pelicula.director,
            'actores': ', '.join(pelicula.actores)
        })

def guardar_cancion(cancion):
    archivo_canciones = 'canciones.csv'
    columnas = ['titulo', 'genero', 'fecha_publicacion', 'album', 'artista']
    necesita_encabezado = not os.path.exists(archivo_canciones)
    
    with open(archivo_canciones, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columnas)
        if necesita_encabezado:
            writer.writeheader()
        writer.writerow({
            'titulo': cancion.titulo,
            'genero': cancion.genero,
            'fecha_publicacion': cancion.fecha_publicacion,
            'album': cancion.album,
            'artista': cancion.artista
        })

def mostrar_peliculas():
    archivo_peliculas = 'peliculas.csv'
    try:
        with open(archivo_peliculas, 'r', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            print("\nPelículas encontradas:")
            for pelicula in lector:
                print(f"Título: {pelicula['titulo']}, Género: {pelicula['genero']}, Año de Publicación: {pelicula['fecha_publicacion']}, Director: {pelicula['director']}, Actores: {pelicula['actores']}")
    except FileNotFoundError:
        print("No se encontraron películas.")

def mostrar_canciones():
    archivo_canciones = 'canciones.csv'
    try:
        with open(archivo_canciones, 'r', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            print("\nCanciones encontradas:")
            for cancion in lector:
                print(f"Título: {cancion['titulo']}, Género: {cancion['genero']}, Año de Publicación: {cancion['fecha_publicacion']}, Álbum: {cancion['album']}, Artista: {cancion['artista']}")
    except FileNotFoundError:
        print("No se encontraron canciones.")

def agregar_pelicula():
    print("\nAgregar nueva película")
    titulo = input("Título: ")
    genero = input("Género: ")
    fecha_publicacion = input("Año de Publicación : ")
    director = input("Director: ")
    actores = input("Actores (separados por comas): ").split(',')
    nueva_pelicula = Peliculas(titulo, genero, fecha_publicacion, director, actores)
    guardar_pelicula(nueva_pelicula)
    print("Película agregada exitosamente.")

def agregar_cancion():
    print("\nAgregar nueva canción")
    titulo = input("Título: ")
    genero = input("Género: ")
    fecha_publicacion = input("Año de Publicación: ")
    album = input("Álbum: ")
    artista = input("Artista: ")
    nueva_cancion = Canciones(titulo, genero, fecha_publicacion, album, artista)
    guardar_cancion(nueva_cancion)
    print("Canción agregada exitosamente.")

def informacion_plataforma():
    print("\nInformación sobre la Plataforma")
    print("Nombre de la Plataforma: Tico Prime Music & Video")
    print("Fecha de Creación: Abril de 2024")
    print("Creadores : Diego Ramirez , Jhonny Jimenez y Luis Alvarez")
    print("Lenguaje de Programación: Python")
    print("Librerías principales: os, csv, pandas")
    print("Descripción: Esta aplicación permite gestionar una colección de canciones y películas.")
    print("Se pueden agregar nuevos registros, ver la lista existente, y aplicar filtros sobre los datos almacenados para mejorar la experienca de busqueda.")

def mostrar_menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Ver Canciones")
        print("2. Ver Películas")
        print("3. Agregar Canción")
        print("4. Agregar Película")
        print("5. Acerca de")
        print("6. Salir\n")
        eleccion = input("Elige una opción: ")
        if eleccion == '1':
            while True:
                print("1. Ver Todas las canciones")
                print("2. Ver filtros de canciones")
                print("3. Salir\n")
                eleccion = input("Elige una opción: ")
                if eleccion == '1':
                    mostrar_canciones()
                    break
                elif eleccion == '2':
                    mostrar_filtros('canciones.csv')
                    break
                elif eleccion == '3':
                    print("Volver al menu principal.\n")
                    break
                else:
                    print("Opción no válida, por favor intenta de nuevo.\n")
        elif eleccion == '2':
            while True:
                print("1. Ver Todas las Películas")
                print("2. Ver filtros de Películas")
                print("3. Salir\n")
                eleccion = input("Elige una opción: ")
                if eleccion == '1':
                    mostrar_peliculas()
                    break
                elif eleccion == '2':
                    mostrar_filtros('peliculas.csv')
                    break
                elif eleccion == '3':
                    print("Volver al menu principal.\n")
                    break
                else:
                    print("Opción no válida, por favor intenta de nuevo.\n")
        elif eleccion == '3':
            agregar_cancion()
        elif eleccion == '4':
            agregar_pelicula()
        elif eleccion == '5':
            informacion_plataforma()
        elif eleccion == '6':
            print("Gracias por usar la aplicación.\n")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.\n")

def mostrar_filtros(archivo):
    # Lee el archivo CSV y carga los datos en un DataFrame de Pandas
    df = pd.read_csv(archivo)
    
    # Obtiene los nombres de las columnas del DataFrame y los convierte en una lista
    columnas = df.columns.tolist()
    
    # Imprime un mensaje indicando que se van a mostrar los filtros disponibles
    print("\nFiltros Disponibles:")
    
    # Itera sobre la lista de columnas y muestra el índice y nombre de cada columna
    for i, columna in enumerate(columnas, 1):
        print(f"{i}. {columna}")
    print()
    
    try:
        # Solicita al usuario que elija una columna para aplicar el filtro
        filtro_seleccionado = int(input("Elige un filtro: "))
          
        # Obtiene el nombre de la columna seleccionada
        columna_seleccionada = columnas[filtro_seleccionado - 1]

    except (ValueError, IndexError):
        # Manejo de errores si la selección no es válida
        print("Selección no válida.\n")
        return
    
    # Obtiene los valores únicos de la columna seleccionada
    valores_unicos = df[columna_seleccionada].unique()
    
    # Imprime una lista numerada de los valores únicos para que el usuario elija uno como criterio de filtro
    for i, valor in enumerate(valores_unicos, 1):
        print(f"{i}. {valor}")
    
    try:
        # Solicita al usuario que elija un valor para aplicar como filtro
        valor_seleccionado = int(input("\nElige un valor para filtrar: "))
        
        # Obtiene el valor seleccionado
        valor = valores_unicos[valor_seleccionado - 1]
    except (ValueError, IndexError):
        # Manejo de errores si la selección no es válida
        print("Selección no válida.\n")
        return
    
    # Crea un nuevo DataFrame filtrando las filas donde el valor de la columna seleccionada coincide con el valor seleccionado
    df_filtrado = df[df[columna_seleccionada] == valor]
    
    # Comprueba si el DataFrame filtrado contiene alguna fila
    if len(df_filtrado) > 0:
        # Imprime un mensaje indicando que se encontraron resultados
        print("\nResultados del filtro:")
        
        # Itera sobre cada fila del DataFrame filtrado y muestra los valores de las columnas relevantes
        for index, row in df_filtrado.iterrows():
            print(f"\n{row['titulo']} - {row['genero']} - {row['fecha_publicacion']}")
            
            # Si hay columnas adicionales como 'album' y 'artista' para canciones, o 'director' y 'actores' para películas, también se imprimen estos detalles
            if 'album' in row and 'artista' in row:
                print(f"Álbum: {row['album']}, Artista: {row['artista']}")
            if 'director' in row and 'actores' in row:
                print(f"Director: {row['director']}, Actores: {row['actores']}")


if __name__ == '__main__':
    mostrar_menu_principal()
