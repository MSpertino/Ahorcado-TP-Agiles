import os

from flask import Flask, redirect, render_template, request, session

from src.domain.ahorcado import Ahorcado, EntradaInvalida

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = os.environ.get("SECRET_KEY", "dev")

    @app.route("/")
    def index():
        if "letra" not in request.args or "palabra" not in session:
            session["palabra"] = request.args.get("word", "GATO")
            session["letras"] = []
        juego = Ahorcado(session["palabra"])
        for letra in session["letras"]:
            juego.arriesgar(letra)
        error = ""
        if "letra" in request.args:
            try:
                juego.arriesgar(request.args["letra"])
                session["letras"] = session["letras"] + [request.args["letra"]]
            except EntradaInvalida as e:
                error = str(e)
        return render_template("index.html", word=juego.palabra_enmascarada(), palabra=session["palabra"], error=error, intentos=juego.intentos_restantes, resultado=juego.resultado(), palabra_revelada=juego.palabra_revelada())

    @app.route("/nueva")
    def nueva():
        session.clear()
        return redirect("/")

    return app

# El botón de encendido
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)