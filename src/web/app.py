from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__, template_folder="templates")

    @app.route("/")
    def index():
        word = request.args.get("word", "")
        hidden_word = " ".join("_" for _ in word)
        return render_template("index.html", word=hidden_word)

    return app