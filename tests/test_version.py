from src.web.app import create_app


def test_version_devuelve_el_commit_desplegado(monkeypatch):
    monkeypatch.setenv("RENDER_GIT_COMMIT", "abc123")
    respuesta = create_app().test_client().get("/version")
    assert respuesta.status_code == 200
    assert respuesta.get_data(as_text=True) == "abc123"
