from pytest_bdd import scenarios, then, parsers

scenarios("../jugar_de_nuevo.feature")

@then(parsers.parse('se ve el botón "{texto}"'))
def entonces_ve_boton(page, texto):
    assert page.get_by_test_id("jugar-de-nuevo").text_content(timeout=2000) == texto
