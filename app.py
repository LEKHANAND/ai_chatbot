from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # ✅ allow GitHub Pages to talk to Render
@app.route("/")
def health():
    return "AI Chatbot backend is running 🚀"
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "").lower()

    if "hello" in user_msg or "hi" in user_msg:
        reply = "Hello! 👋 How can I help you?"
    elif "name" in user_msg:
        reply = "I am your AI chatbot 🤖"
    elif "bye" in user_msg:
        reply = "Goodbye! Have a nice day 👋"
    else:
        reply = "Sorry, I am still learning 😅"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()



