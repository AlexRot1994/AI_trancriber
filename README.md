# Audio Transcriber mit OpenAI Whisper API

Ein einfaches Projekt, um Audiodateien per Streamlit mit der OpenAI Whisper API zu transkribieren.

## Anforderungen

- OpenAI API Key (https://platform.openai.com/account/api-keys)

## Lokale Ausführung

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Geheimnis hinzufügen (für Streamlit Cloud)

In Streamlit Cloud unter "Secrets" folgendes hinzufügen:

- `OPENAI_API_KEY`: dein API-Key von OpenAI