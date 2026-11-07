from pytest_bdd import scenarios, then, parsers

scenarios("../letras_usadas.feature")

@then(parsers.parse('se ven las letras usadas "{esperadas}"'))
def entonces_ve_letras_usadas(page, esperadas):
    assert page.get_by_test_id("letras-usadas").text_content(timeout=2000) == esperadas

@then(parsers.parse('se ven las letras acertadas "{esperadas}"'))
def entonces_ve_letras_acertadas(page, esperadas):
    assert page.get_by_test_id("letras-acertadas").text_content(timeout=2000) == esperadas

@then(parsers.parse('se ven las letras falladas "{esperadas}"'))
def entonces_ve_letras_falladas(page, esperadas):
    assert page.get_by_test_id("letras-falladas").text_content(timeout=2000) == esperadas