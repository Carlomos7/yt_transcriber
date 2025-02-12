import streamlit as st
import requests

# API Base URL
API_URL = "http://127.0.0.1:8000"

# Streamlit Page Setup
st.set_page_config(page_title="YouTube Transcriber", page_icon="🎵", layout="centered")

# Title & Introduction
st.title("🎵 YouTube Transcriber")
st.markdown(
    """
    **Convert YouTube videos into text effortlessly!**  
    Enter a **YouTube URL** and choose from the following actions:
    - 🎶 **Download Audio**: Extract and save the video's audio.
    - 🎥 **Download Video**: Download the full video.
    - 📝 **Transcribe Audio**: Automatically download the audio and generate text.
    """
)

# User Input for YouTube URL
yt_url = st.text_input("🔗 **Enter YouTube URL:**", placeholder="https://www.youtube.com/watch?v=EXAMPLE")

# Store paths in session state
if "audio_file_path" not in st.session_state:
    st.session_state["audio_file_path"] = None
if "video_file_path" not in st.session_state:
    st.session_state["video_file_path"] = None
if "transcription_text" not in st.session_state:
    st.session_state["transcription_text"] = None

# Buttons for Actions
st.divider()
st.subheader("🛠 **Choose an Action:**")

col1, col2, col3 = st.columns(3)

with col1:
    transcribe_btn = st.button("📝 Transcribe Audio")
with col2:
    download_audio_btn = st.button("🎶 Download Audio")
with col3:
    download_video_btn = st.button("🎥 Download Video")

# API Calls & Handling
if yt_url:
    if download_audio_btn:
        st.subheader("🎶 **Downloading Audio...**")
        with st.spinner("Processing request..."):
            audio_response = requests.post(f"{API_URL}/download/audio/", json={"url": yt_url})

        if audio_response.status_code == 200:
            st.session_state["audio_file_path"] = audio_response.json()["file_path"]
            st.success(f"✅ **Audio saved at:** `{st.session_state['audio_file_path']}`")
        else:
            st.error("❌ Audio download failed. Please check the URL and try again.")

    if transcribe_btn:
        st.subheader("📝 **Transcribing Audio...**")
        with st.spinner("Downloading audio and generating text..."):
            transcribe_response = requests.post(f"{API_URL}/transcribe/", json={"url": yt_url})  # ✅ Fix: Sending URL, not file path

        if transcribe_response.status_code == 200:
            st.session_state["transcription_text"] = transcribe_response.json()["transcription"]
            st.success("✅ **Transcription completed successfully!**")
            st.subheader("📜 **Transcribed Text:**")
            st.write(st.session_state["transcription_text"])

            # Provide Download Option
            st.download_button(
                label="💾 Download Transcription",
                data=st.session_state["transcription_text"],
                file_name="transcription.txt",
                mime="text/plain",
            )
        else:
            st.error("❌ Transcription failed. Please try again.")

    if download_video_btn:
        st.subheader("🎥 **Downloading Video...**")
        with st.spinner("Processing request..."):
            video_response = requests.post(f"{API_URL}/download/video/", json={"url": yt_url})

        if video_response.status_code == 200:
            st.session_state["video_file_path"] = video_response.json()["file_path"]
            st.success(f"✅ **Video saved at:** `{st.session_state['video_file_path']}`")
        else:
            st.error("❌ Video download failed. Please check the URL and try again.")

# Add spacing for better UI
st.divider()
st.caption("🔹 Developed with ❤️ using FastAPI, Whisper, and Streamlit.")
