from flask import Flask, render_template, request

from src.domain.ahorcado import Ahorcado, EntradaInvalida

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    @app.route("/")
    def index():
        palabra = request.args.get("word", "")
        oculta = " ".join("_" for _ in palabra)
        error = ""
        if "letra" in request.args:
            try:
                Ahorcado(palabra).arriesgar(request.args["letra"])
            except EntradaInvalida as e:
                error = str(e)
        return render_template("index.html", word=oculta, palabra=palabra, error=error)

    return app

# El botón de encendido
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)