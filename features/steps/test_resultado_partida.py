from pytest_bdd import scenarios, then, parsers

scenarios("../resultado_partida.feature")

@then(parsers.parse('se ve el mensaje de resultado "{mensaje}"'))
def entonces_ve_mensaje_resultado(page, mensaje):
    resultado_el = page.get_by_test_id("resultado")
    assert resultado_el.text_content(timeout=2000) == mensaje