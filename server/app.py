from flask import Flask

app = Flask(__name__)

existing_models = ["Beedle", "Crossroads", "M2", "Panique"]


@app.route("/")
def index():
    return "<h1>Welcome to Flatiron Cars</h1>"


@app.route("/<string:model>")
def request_a_model(model):
    if model not in existing_models:
        return f"<h1>No models called {model} exists in our catalog</h1>"

    return f"<h1>Flatiron {model} is in our fleet!</h1>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
