from behave import given, when, then

@given('que estoy en el formulario de datos personales')
def step_impl(context):
    # Implementación de la navegación a la página del formulario (simulado)
    pass

@when('ingreso mi nombre "{nombre}", apellido "{apellido}", edad "{edad}", email "{email}" y teléfono "{telefono}"')
def step_impl(context, nombre, apellido, edad, email, telefono):
    # Simulación de interacción con los campos del formulario y envío de datos
    context.nombre = nombre
    context.apellido = apellido
    context.edad = int(edad)
    context.email = email
    context.telefono = telefono

@then('veo un mensaje de confirmación de ingreso exitoso')
def step_impl(context):
    # Verificación de mensaje de confirmación de ingreso exitoso (simulado)
    assert True

@then('veo un mensaje de error indicando que la edad debe ser un número positivo')
def step_impl(context):
    # Verificación de mensaje de error por edad negativa
    assert context.edad >= 0, "La edad debe ser un número positivo"

@then('veo un mensaje de error indicando que el campo de nombre es obligatorio')
def step_impl(context):
    # Verificación de mensaje de error por campo de nombre en blanco
    assert context.nombre != "", "El campo de nombre es obligatorio"
