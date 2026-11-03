from pytest_bdd import scenarios, then, parsers

scenarios("../soporte_acentos.feature")

@then(parsers.parse('se ve la palabra "{esperada}"'))
def entonces_se_ve_palabra(page, esperada):
    assert page.get_by_test_id("word").text_content() == esperada