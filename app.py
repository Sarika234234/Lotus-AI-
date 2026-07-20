from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_reply(message):
    message = message.lower()

    if "hi" in message or "hello" in message:
        return "Hello! I am Lotus AI."

    elif "how are you" in message:
        return "I'm doing great! Thanks for asking."

    elif "your name" in message:
        return "My name is Lotus AI."

    elif "python" in message:
        return "Python is a powerful programming language."

    elif "bye" in message:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't know that yet."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    reply = get_reply(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
