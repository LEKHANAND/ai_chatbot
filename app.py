import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # allow GitHub Pages to call Render

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def health():
    return "AI Chatbot backend is running 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    if not user_msg:
        return jsonify({"reply": "Please type something."})

    try:
        response = model.generate_content(user_msg)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)







