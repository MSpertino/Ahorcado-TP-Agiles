from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__, template_folder="templates")

    @app.route("/")
    def index():
        return render_template("index.html", word="_ _ _ _")

    return app