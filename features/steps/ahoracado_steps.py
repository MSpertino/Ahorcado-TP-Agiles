from behave import given, then
from playwright.sync_api import expect

@given('una partida con la palabra "{palabra}"')
def step_iniciar_partida(context, palabra):
    # Flask por defecto corre en el puerto 5000. 
    # Usamos la URL para inyectar la palabra secreta (nuestro seam).
    context.page.goto(f"http://127.0.0.1:5000/?word={palabra}")

@then('se ve la palabra oculta "{esperada}"')
def step_ver_palabra(context, esperada):
    # Buscamos en el HTML un elemento con el atributo data-testid="word"
    elemento_palabra = context.page.locator('[data-testid="word"]')
    # Verificamos que contenga exactamente los guiones esperados
    expect(elemento_palabra).to_have_text(esperada)