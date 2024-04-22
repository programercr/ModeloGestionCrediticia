import unittest
import os
import csv
import sys
from io import StringIO
from StreamingPOO import guardar_pelicula, Peliculas, guardar_cancion, Canciones, mostrar_peliculas, mostrar_canciones, informacion_plataforma




class TestGuardarPelicula(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de la clase Peliculas para usar en las pruebas
        self.pelicula_prueba = Peliculas(
            titulo="Ejemplo de Película",
            genero="Acción",
            fecha_publicacion="2023",
            director="Director Ejemplo",
            actores=["Actor1", "Actor2"]
        )

    def tearDown(self):
        # Eliminar el archivo de películas creado durante las pruebas
        if os.path.exists('peliculas.csv'):
            os.remove('peliculas.csv')

    def test_guardar_pelicula(self):
        # Llamar a la función guardar_pelicula con la película de prueba
        guardar_pelicula(self.pelicula_prueba)

        # Verificar si el archivo de películas ha sido creado
        self.assertTrue(os.path.exists('peliculas.csv'))

        # Leer el archivo de películas y verificar si los datos de la película están presentes
        with open('peliculas.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            row = next(reader)
            self.assertEqual(row['titulo'], self.pelicula_prueba.titulo)
            self.assertEqual(row['genero'], self.pelicula_prueba.genero)
            self.assertEqual(row['fecha_publicacion'], self.pelicula_prueba.fecha_publicacion)
            self.assertEqual(row['director'], self.pelicula_prueba.director)



class TestGuardarCancion(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de la clase Canciones para usar en las pruebas
        self.cancion_prueba = Canciones(
            titulo="Ejemplo de Canción",
            genero="Pop",
            fecha_publicacion="2022",
            album="Álbum de Ejemplo",
            artista="Artista Ejemplo"
        )

    def tearDown(self):
        # Eliminar el archivo de canciones creado durante las pruebas
        if os.path.exists('canciones.csv'):
            os.remove('canciones.csv')

    def test_guardar_cancion(self):
        # Llamar a la función guardar_cancion con la canción de prueba
        guardar_cancion(self.cancion_prueba)

        # Verificar si el archivo de canciones ha sido creado
        self.assertTrue(os.path.exists('canciones.csv'))

        # Leer el archivo de canciones y verificar si los datos de la canción están presentes
        with open('canciones.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            row = next(reader)
            self.assertEqual(row['titulo'], self.cancion_prueba.titulo)
            self.assertEqual(row['genero'], self.cancion_prueba.genero)
            self.assertEqual(row['fecha_publicacion'], self.cancion_prueba.fecha_publicacion)
            self.assertEqual(row['album'], self.cancion_prueba.album)
            self.assertEqual(row['artista'], self.cancion_prueba.artista)

class TestMostrarPeliculas(unittest.TestCase):
    def setUp(self):
        # Crear un archivo de películas de prueba con datos simulados
        with open('peliculas.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['titulo', 'genero', 'fecha_publicacion', 'director', 'actores'])
            writer.writeheader()
            writer.writerow({
                'titulo': 'Pelicula de Prueba',
                'genero': 'Comedia',
                'fecha_publicacion': '2022',
                'director': 'Director de Prueba',
                'actores': 'Actor1, Actor2'
            })

    def tearDown(self):
        # Eliminar el archivo de películas creado durante las pruebas
        if os.path.exists('peliculas.csv'):
            os.remove('peliculas.csv')

    def test_mostrar_peliculas(self):
        # Capturar la salida estándar para verificarla
        captured_output = StringIO()
        sys.stdout = captured_output

        # Llamar a la función mostrar_peliculas
        mostrar_peliculas()

        # Restaurar la salida estándar
        sys.stdout = sys.__stdout__

        # Verificar si la salida contiene los datos de la película de prueba
        output_str = captured_output.getvalue().strip()
        self.assertIn('Pelicula de Prueba', output_str)
        self.assertIn('Comedia', output_str)
        self.assertIn('2022', output_str)
        self.assertIn('Director de Prueba', output_str)
        self.assertIn('Actor1, Actor2', output_str)


class TestMostrarPeliculas(unittest.TestCase):
    def setUp(self):
        # Crear un archivo de películas de prueba con datos simulados
        with open('peliculas.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['titulo', 'genero', 'fecha_publicacion', 'director', 'actores'])
            writer.writeheader()
            writer.writerow({
                'titulo': 'Pelicula de Prueba',
                'genero': 'Comedia',
                'fecha_publicacion': '2022',
                'director': 'Director de Prueba',
                'actores': 'Actor1, Actor2'
            })

    def tearDown(self):
        # Eliminar el archivo de películas creado durante las pruebas
        if os.path.exists('peliculas.csv'):
            os.remove('peliculas.csv')

    def test_mostrar_peliculas(self):
        # Capturar la salida estándar para verificarla
        captured_output = StringIO()
        sys.stdout = captured_output

        # Llamar a la función mostrar_peliculas
        mostrar_peliculas()

        # Restaurar la salida estándar
        sys.stdout = sys.__stdout__

        # Verificar si la salida contiene los datos de la película de prueba
        output_str = captured_output.getvalue().strip()
        self.assertIn('Pelicula de Prueba', output_str)
        self.assertIn('Comedia', output_str)
        self.assertIn('2022', output_str)
        self.assertIn('Director de Prueba', output_str)
        self.assertIn('Actor1, Actor2', output_str)

class TestMostrarCanciones(unittest.TestCase):
    def setUp(self):
        # Crear un archivo de canciones de prueba con datos simulados
        with open('canciones.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['titulo', 'genero', 'fecha_publicacion', 'album', 'artista'])
            writer.writeheader()
            writer.writerow({
                'titulo': 'Cancion de Prueba',
                'genero': 'Pop',
                'fecha_publicacion': '2022',
                'album': 'Álbum de Prueba',
                'artista': 'Artista de Prueba'
            })

    def tearDown(self):
        # Eliminar el archivo de canciones creado durante las pruebas
        if os.path.exists('canciones.csv'):
            os.remove('canciones.csv')

    def test_mostrar_canciones(self):
        # Capturar la salida estándar para verificarla
        captured_output = StringIO()
        sys.stdout = captured_output

        # Llamar a la función mostrar_canciones
        mostrar_canciones()

        # Restaurar la salida estándar
        sys.stdout = sys.__stdout__

        # Verificar si la salida contiene los datos de la canción de prueba
        output_str = captured_output.getvalue().strip()
        self.assertIn('Cancion de Prueba', output_str)
        self.assertIn('Pop', output_str)
        self.assertIn('2022', output_str)
        self.assertIn('Álbum de Prueba', output_str)
        self.assertIn('Artista de Prueba', output_str)


class TestInformacionPlataforma(unittest.TestCase):
    def test_informacion_plataforma(self):
        # Capturar la salida estándar para verificarla
        captured_output = StringIO()
        sys.stdout = captured_output

        # Llamar a la función informacion_plataforma
        informacion_plataforma()

        # Restaurar la salida estándar
        sys.stdout = sys.__stdout__

        # Verificar si la salida contiene la información esperada
        output_str = captured_output.getvalue().strip()
        self.assertIn('Nombre de la Plataforma: Tico Prime Music & Video', output_str)
        self.assertIn('Fecha de Creación: Abril de 2024', output_str)
        self.assertIn('Creadores : Diego Ramirez , Jhonny Jimenez y Luis Alvarez', output_str)
        self.assertIn('Lenguaje de Programación: Python', output_str)
        self.assertIn('Librerías principales: os, csv, pandas', output_str)
        self.assertIn('Descripción: Esta aplicación permite gestionar una colección de canciones y películas.', output_str)
        self.assertIn('Se pueden agregar nuevos registros, ver la lista existente, y aplicar filtros sobre los datos almacenados para mejorar la experienca de busqueda.', output_str)


class TestClasesHijas(unittest.TestCase):
    def test_instancia_canciones(self):
        cancion = Canciones(
            titulo="Canción de Prueba",
            genero="Pop",
            fecha_publicacion="2022",
            album="Álbum de Prueba",
            artista="Artista de Prueba"
        )
        self.assertIsInstance(cancion, Canciones)
        self.assertEqual(cancion.titulo, "Canción de Prueba")
        self.assertEqual(cancion.genero, "Pop")
        self.assertEqual(cancion.fecha_publicacion, "2022")
        self.assertEqual(cancion.album, "Álbum de Prueba")
        self.assertEqual(cancion.artista, "Artista de Prueba")

    def test_instancia_peliculas(self):
        pelicula = Peliculas(
            titulo="Pelicula de Prueba",
            genero="Comedia",
            fecha_publicacion="2022",
            director="Director de Prueba",
            actores=["Actor1", "Actor2"]
        )
        self.assertIsInstance(pelicula, Peliculas)
        self.assertEqual(pelicula.titulo, "Pelicula de Prueba")
        self.assertEqual(pelicula.genero, "Comedia")
        self.assertEqual(pelicula.fecha_publicacion, "2022")
        self.assertEqual(pelicula.director, "Director de Prueba")
        self.assertListEqual(pelicula.actores, ["Actor1", "Actor2"])

if __name__ == '__main__':
    unittest.main()

