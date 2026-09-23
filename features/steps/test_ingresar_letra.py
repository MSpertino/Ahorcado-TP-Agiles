from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../ingresar_letra.feature")

@then("no se ve ningún mensaje de error")
def entonces_no_hay_error(page):
    error_el = page.get_by_test_id("error-message")
    assert error_el.text_content() == ""

@then("se ve un mensaje de entrada rechazada")
def entonces_hay_error(page):
    error_el = page.get_by_test_id("error-message")
    assert error_el.text_content() == "Solo se permite una letra por vez"