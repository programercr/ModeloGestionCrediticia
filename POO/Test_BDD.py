# Importamos las librerías necesarias
from behave import given, when, then

# Definimos los pasos iniciales usando el decorador @given
@given('una calculadora')
def step_impl(context):
    context.calculadora = Calculadora()

# Definimos los pasos para la acción que queremos probar usando el decorador @when
@when('sumamos {x:d} y {y:d}')
def step_impl(context, x, y):
    context.resultado = context.calculadora.sumar(x, y)

# Definimos los pasos para la verificación del resultado usando el decorador @then
@then('el resultado es {resultado:d}')
def step_impl(context, resultado):
    assert context.resultado == resultado, f"El resultado debería ser {resultado} pero fue {context.resultado}"

# Clase de la calculadora
class Calculadora:
    def sumar(self, x, y):
        return x + y
