import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../iniciar_partida.feature")

@given(parsers.parse('una partida con la palabra "{palabra}"'), target_fixture="palabra_partida")
def dado_partida(palabra):
    return palabra

@then(parsers.parse('se ve la palabra "{esperada}"'))
def ve_palabra(page, palabra_partida, esperada, live_server):
    page.goto(f"{live_server.url()}/?word={palabra_partida}")
    assert page.get_by_test_id("word").text_content() == esperada

@then(parsers.parse("se ven {vidas:d} vidas"))
def ve_vidas(page, vidas):
    assert page.get_by_test_id("lives").text_content() == str(vidas)