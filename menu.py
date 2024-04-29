from tipo_cliente import *
from productos_crediticios import *


while True:
      print('''
      Bienvenido al sistema de gestion Crediticia

      Iniciaremos el registro de cliente

      Seleccione el tipo de empleo:
      1. Asalariado
      2. Independiente
      3. Pensionado

      ''')
      id = tipo_empleo()
      analizador = AnalizadorDeUsuarios("usuarios.csv")
      analizador.agregar_cuota()
      info_usuario, info_productos = analizador.productos(id)
      print(info_productos.to_string(index=False))
      producto_seleccionado = analizador.elegir_producto()
      info_producto = analizador.usuario_producto(info_usuario, producto_seleccionado)




