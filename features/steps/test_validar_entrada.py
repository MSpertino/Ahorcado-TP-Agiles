from pytest_bdd import scenarios, then, parsers

scenarios("../validar_entrada.feature")

@then(parsers.parse('se ve el mensaje de error "{mensaje}"'))
def entonces_ve_mensaje_error(page, mensaje):
    error_el = page.get_by_test_id("error-message")
    assert error_el.text_content() == mensaje
