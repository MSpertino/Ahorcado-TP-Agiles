from pytest_bdd import scenarios, then, parsers

scenarios("../ver_intentos.feature")

@then(parsers.parse("se ven {intentos:d} intentos restantes"))
def entonces_ve_intentos(page, intentos):
    assert page.get_by_test_id("intentos").text_content() == str(intentos)
