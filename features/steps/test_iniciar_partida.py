import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../iniciar_partida.feature")

@then(parsers.parse('se ve la palabra "{esperada}"'))
def ve_palabra(page, esperada):
    assert page.get_by_test_id("word").text_content() == esperada