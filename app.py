from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"].lower()

    # Simple chatbot logic
    if "hello" in user_msg:
        reply = "Hello! How can I help you?"
    elif "name" in user_msg:
        reply = "I am your AI chatbot 😄"
    elif "bye" in user_msg:
        reply = "Goodbye! Have a nice day 👋"
    else:
        reply = "Sorry, I am still learning 🤖"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
