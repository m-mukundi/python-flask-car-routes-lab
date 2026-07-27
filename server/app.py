from flask import Flask

app = Flask(__name__)

existing_models = ["Beedle", "Crossroads", "M2", "Panique"]


@app.route("/")
def index():
    return "Welcome to Flatiron Cars"


@app.route("/<string:model>")
def request_a_model(model):
    if model not in existing_models:
        return f"No models called {model} exists in our catalog"

    return f"Flatiron {model} is in our fleet!"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
