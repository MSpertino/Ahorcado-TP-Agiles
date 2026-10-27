import threading
from types import SimpleNamespace

import pytest
from playwright.sync_api import sync_playwright
from werkzeug.serving import make_server

from src.web.app import create_app

from pytest_bdd import given, when, parsers, then

@given(parsers.parse('una partida con la palabra "{palabra}"'), target_fixture="palabra_partida")
def dado_partida(page, live_server, palabra):
    page.goto(f"{live_server.url()}/?word={palabra}")
    return palabra

@when(parsers.parse('el jugador ingresa la letra "{letra}"'))
def cuando_ingresa_letra(page, letra):
    input_el = page.get_by_test_id("letra-input")
    input_el.fill(letra)
    input_el.press("Enter")

@pytest.fixture(scope="session")
def app():
    return create_app()

@pytest.fixture(scope="session")
def live_server(app):
    server = make_server("127.0.0.1", 0, app)
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    def url():
        return f"http://127.0.0.1:{port}"

    yield SimpleNamespace(url=url)

    server.shutdown()
    thread.join()
    server.server_close()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close() 

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@then(parsers.parse("se ven {intentos:d} intentos restantes"))
def entonces_ve_intentos(page, intentos):
    assert page.get_by_test_id("intentos").text_content() == str(intentos)

@when("el jugador abre el juego sin indicar palabra")
def abrir_juego_sin_palabra(page, live_server):
    page.goto(f"{live_server.url()}/")

@then(parsers.parse('se ve el mensaje de error "{mensaje}"'))
def entonces_ve_mensaje_error(page, mensaje):
    error_el = page.get_by_test_id("error-message")
    assert error_el.text_content() == mensaje

@then(parsers.parse('se ve el mensaje de resultado "{mensaje}"'))
def entonces_ve_mensaje_resultado(page, mensaje):
    resultado_el = page.get_by_test_id("resultado")
    assert resultado_el.text_content(timeout=2000) == mensaje
