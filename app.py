from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import re

app = Flask(__name__)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")
def sanitize_message(message):
    # Remove email addresses
    message = re.sub(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        '[EMAIL REDACTED]',
        message
    )

    # Remove phone numbers (10–15 digits with optional spaces or dashes)
    message = re.sub(
        r'\b(?:\+?\d[\d\s-]{8,14}\d)\b',
        '[PHONE REDACTED]',
        message
    )

    return message

def get_reply(message):
    # Keep a clean version of the message
    clean_message = sanitize_message(
    "Never ask for or store passwords, OTPs, bank details, government IDs or other highly sensitive personal information. "
    + message
)

    try:
        response = model.generate_content(clean_message)

        if response.text:
            return response.text

        return "Sorry, I couldn't generate a response."

    except Exception:
        # Fallback if Gemini is unavailable
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
            return "Sorry, Lotus AI is temporarily unavailable."

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
