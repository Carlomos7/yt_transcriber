import streamlit as st
import requests

# API Base URL
API_URL = "http://127.0.0.1:8000"

# Streamlit Page Setup
st.set_page_config(page_title="YouTube Transcriber", page_icon="🎵", layout="centered")

st.title("🎵 YouTube Transcriber")
st.write("Enter a YouTube URL and choose an option.")

# User Input for YouTube URL
yt_url = st.text_input("🔗 Enter YouTube URL:", placeholder="https://www.youtube.com/watch?v=EXAMPLE")

# Store paths in session state
if "audio_file_path" not in st.session_state:
    st.session_state["audio_file_path"] = None
if "video_file_path" not in st.session_state:
    st.session_state["video_file_path"] = None
if "transcription_text" not in st.session_state:
    st.session_state["transcription_text"] = None

# Buttons for Actions
col1, col2, col3 = st.columns(3)

with col1:
    transcribe_btn = st.button("📝 Transcribe (Auto)")
with col2:
    download_audio_btn = st.button("🎶 Download Audio")
with col3:
    download_video_btn = st.button("🎥 Download Video")

# API Calls & Handling
if yt_url:
    if download_audio_btn:
        with st.spinner("Downloading audio..."):
            audio_response = requests.post(f"{API_URL}/download/audio/", json={"url": yt_url})

        if audio_response.status_code == 200:
            st.session_state["audio_file_path"] = audio_response.json()["file_path"]
            st.success(f"✅ Audio downloaded: `{st.session_state['audio_file_path']}`")
        else:
            st.error("❌ Audio download failed.")

    if transcribe_btn:
        with st.spinner("Transcribing audio..."):
            transcribe_response = requests.post(f"{API_URL}/transcribe/", json={"url": yt_url})  # ✅ Fix: Send `url`, not `file_path`

        if transcribe_response.status_code == 200:
            st.session_state["transcription_text"] = transcribe_response.json()["transcription"]
            st.subheader("📝 Transcribed Text:")
            st.write(st.session_state["transcription_text"])

            # Provide Download Option
            st.download_button(
                label="💾 Download Transcription",
                data=st.session_state["transcription_text"],
                file_name="transcription.txt",
                mime="text/plain",
            )
        else:
            st.error("❌ Transcription failed. Check the URL.")

    if download_video_btn:
        with st.spinner("Downloading video..."):
            video_response = requests.post(f"{API_URL}/download/video/", json={"url": yt_url})

        if video_response.status_code == 200:
            st.session_state["video_file_path"] = video_response.json()["file_path"]
            st.success(f"✅ Video downloaded: `{st.session_state['video_file_path']}`")
        else:
            st.error("❌ Video download failed.")
