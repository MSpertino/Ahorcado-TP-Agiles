import threading
from types import SimpleNamespace

import pytest
from playwright.sync_api import sync_playwright
from werkzeug.serving import make_server

from src.web.app import create_app

from pytest_bdd import given, parsers

@given(parsers.parse('una partida con la palabra "{palabra}"'), target_fixture="palabra_partida")
def dado_partida(palabra):
    return palabra

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