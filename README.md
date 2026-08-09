# Lotus AI

Lotus AI is a full-stack conversational AI web application built with Python and Flask, integrating Google's Gemini API for natural-language response generation.

The application combines a Flask backend with a responsive HTML, CSS, and JavaScript frontend to provide a streamlined conversational experience across desktop and mobile devices.

## Features

- AI-powered conversational responses
- Google Gemini API integration
- Responsive web interface
- Flask-based backend
- Asynchronous client-server communication
- JSON-based data exchange
- Structured AI response formatting
- Basic input sanitization
- Privacy and safety acknowledgement
- Cloud deployment

## Technology Stack

### Backend
- Python
- Flask
- Google Gen AI SDK

### Frontend
- HTML5
- CSS3
- JavaScript

### AI
- Google Gemini API

### Deployment
- Render
- Gunicorn

## Architecture

```text
User
 │
 ▼
Web Interface
 │
 ▼
JavaScript
 │
 ▼
Flask Backend
 │
 ▼
Google Gemini API
 │
 ▼
AI Response
 │
 ▼
Web Interface
LotusAI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
## Future Development

- Persistent conversation management
- Database integration
- Streaming AI responses
- Retrieval-Augmented Generation (RAG)
- Automated testing
