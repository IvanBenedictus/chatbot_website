from flask import Flask, render_template, request, jsonify
from chatbot import chatbot

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = chatbot.get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)