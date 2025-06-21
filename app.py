import streamlit as st
import whisper
import tempfile

st.title("🎙️ Audio-Transkription mit KI")
st.write("Lade eine Audiodatei hoch (mp3, wav, m4a)...")

uploaded_file = st.file_uploader("Audiodatei hochladen", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.info("Transkription läuft, bitte warten...")
    model = whisper.load_model("base")
    result = model.transcribe(tmp_path)
    st.success("Fertig!")
    st.text_area("📝 Transkribierter Text", result["text"], height=300)