# Audio Transcriber mit KI

Ein einfaches Python-Projekt zur Transkription von Audiodateien mit OpenAI Whisper und Streamlit.

## Funktionen
- Unterstützt mp3, wav, m4a
- Echtzeit-Transkription im Browser
- Docker-kompatibel

## Installation lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Mit Docker

```bash
docker build -t audio-transcriber .
docker run -p 8501:8501 audio-transcriber
```