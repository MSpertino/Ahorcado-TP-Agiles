from pytest_bdd import scenarios, then, parsers

scenarios("../revelar_palabra.feature")

@then(parsers.parse('se ve la palabra revelada "{palabra}"'))
def entonces_ve_palabra_revelada(page, palabra):
    assert page.get_by_test_id("palabra-revelada").text_content(timeout=2000) == palabra
