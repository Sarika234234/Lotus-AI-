from flask import Flask, render_template, request, jsonify
from google import genai
import os
import re

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


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

    clean_message = sanitize_message(
        "You are Lotus AI, a helpful, clear, and professional AI assistant. "

        "Never ask for or store passwords, OTPs, bank details, government IDs, "
        "or other highly sensitive personal information. "

        "Answer questions clearly and accurately. "
        "Use a short heading when it improves readability. "
        "When the user asks how to do something or when a process has multiple steps, "
        "use a numbered step-by-step format. "
        "When listing several items, use bullet points. "
        "Use short paragraphs and leave space between different sections. "
        "Bold important terms when appropriate. "
        "Do not put the entire answer into one large paragraph. "
        "Keep answers easy to read on both mobile phones and computers. "

        + message
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=clean_message
        )

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
