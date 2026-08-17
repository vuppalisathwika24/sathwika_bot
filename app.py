from pathlib import Path

import ollama
from flask import Flask, jsonify, request, send_from_directory

MODEL = "llama3.2"
SYSTEM_PROMPT = {"role": "system", "content": "You are a helpful assistant."}

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory(Path(__file__).parent, "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    messages = data.get("messages", [])

    if not messages:
        return jsonify({"error": "No message provided."}), 400

    full_messages = [SYSTEM_PROMPT, *messages]

    try:
        response = ollama.chat(model=MODEL, messages=full_messages)
        reply = response["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Open http://127.0.0.1:5000 in your browser")
    app.run(debug=True)
