from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__, template_folder="templates")

    @app.route("/")
    def index():
        palabra = request.args.get("word", "")
        oculta = " ".join("_" for _ in palabra)
        return render_template("index.html", word=oculta)

    return app

# El botón de encendido
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)