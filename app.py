import streamlit as st
import openai
import tempfile
import os

st.title("🎙️ Audio-Transkription mit OpenAI Whisper API")

openai.api_key = st.secrets["OPENAI_API_KEY"]

uploaded_file = st.file_uploader("Lade eine Audiodatei hoch (mp3, wav, m4a)...", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.info("⏳ Sende Datei an OpenAI...")
    with open(tmp_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    st.success("✅ Transkription abgeschlossen!")
    st.text_area("📝 Transkribierter Text", transcript["text"], height=300)