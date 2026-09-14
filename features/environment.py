from playwright.sync_api import sync_playwright

def before_all(context):
    # Inicia Playwright y abre Chromium una sola vez al arrancar los tests
    context.playwright = sync_playwright().start()
    # headless=True ejecuta el navegador en segundo plano (sin abrir la ventana visual)
    context.browser = context.playwright.chromium.launch(headless=True)

def before_scenario(context, scenario):
    # Abre una pestaña completamente limpia para cada escenario
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    # Cierra la pestaña al terminar el escenario para no dejar basura
    context.page.close()

def after_all(context):
    # Cierra el navegador definitivamente al terminar toda la suite
    context.browser.close()
    context.playwright.stop()