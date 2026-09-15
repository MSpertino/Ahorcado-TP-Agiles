from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../ingresar_letra.feature")

@when(parsers.parse('el jugador ingresa la letra "{letra}"'))
def cuando_ingresa_letra(page, palabra_partida, letra, live_server):
    page.goto(f"{live_server.url()}/?word={palabra_partida}")
    input_el = page.get_by_test_id("letra-input")
    input_el.fill(letra)
    input_el.press("Enter")

@then("no se ve ningún mensaje de error")
def entonces_no_hay_error(page):
    error_el = page.get_by_test_id("error-message")
    assert error_el.text_content() == ""

@then("se ve un mensaje de entrada rechazada")
def entonces_hay_error(page):
    error_el = page.get_by_test_id("error-message")
    assert error_el.text_content() != ""