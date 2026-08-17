# Sathwika Bot

A simple terminal chatbot powered by [Ollama](https://ollama.com) and the `llama3.2` model.

## Prerequisites

1. Install [Ollama](https://ollama.com/download)
2. Pull the model:

```bash
ollama pull llama3.2
```

## Setup

```bash
pip install -r requirements.txt
```

## Run (Terminal)

```bash
python chat.py
```

Type your messages at the `You:` prompt. Type `quit` or `exit` to leave.

## Run (Web)

```bash
pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to chat on the webpage.
