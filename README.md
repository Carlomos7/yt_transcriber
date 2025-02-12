# YouTube Transcriber

## Overview

YouTube Transcriber is a **microservice-based** application that allows users to:

- 🎶 **Download YouTube Audio or Video**
- 📝 **Transcribe Speech to Text** using OpenAI Whisper
- 📜 **Download Transcriptions**
- 🖥 **Interact via FastAPI Backend & Streamlit UI**

Designed with **modularity** to support different transcription engines in the future.

---

## Features

✔️ **YouTube Audio & Video Downloading** (via `yt-dlp`)  
✔️ **Speech-to-Text Transcription** (via OpenAI `Whisper`)  
✔️ **FastAPI API Endpoints for Scalability**  
✔️ **Streamlit Web Interface for Easy Interaction**  
✔️ **Optimized Model Loading & Caching**  
✔️ **Good Project Structure & Extensibility**  

---

## Installation

### Prerequisites

- **Python 3.10+**
- **FFmpeg** (`brew install ffmpeg` or `sudo apt install ffmpeg`)
- **pip & Virtual Environment**

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/youtube-transcriber.git
cd youtube-transcriber
```

### 2️⃣ Create a Virtual Environment & Install Dependencies

```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Create a `.env` file and configure it:

```ini
# .env file
WHISPER_MODEL=small
API_HOST=127.0.0.1
API_PORT=8000
OUTPUT_DIR=downloads
```

---

## Running the Application

### 1️⃣ Start FastAPI Backend

```sh
uvicorn app.main:app --reload
```

➡️ API runs at: **http://127.0.0.1:8000/docs**

### 2️⃣ Run Streamlit UI

```sh
streamlit run streamlit_app.py
```

➡️ UI runs at: **http://localhost:8501**

---

## Usage

### API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST** | `/download/audio/` | Downloads audio from a YouTube URL |
| **POST** | `/download/video/` | Downloads video from a YouTube URL |
| **POST** | `/transcribe/` | Downloads & transcribes YouTube audio |
| **GET**  | `/files/audio/{filename}` | Retrieves a downloaded audio file |
| **GET**  | `/files/video/{filename}` | Retrieves a downloaded video file |
| **GET**  | `/files/text/{filename}` | Retrieves the transcribed text file |

#### Example Request (Download Audio)

```sh
curl -X POST "http://127.0.0.1:8000/download/audio/" -H "Content-Type: application/json" -d '{"url": "https://www.youtube.com/watch?v=EXAMPLE"}'
```

### Streamlit UI

- Enter a **YouTube URL**  
- Click one of the buttons:
  - **🎶 Download Audio**
  - **🎥 Download Video**
  - **📝 Transcribe Audio** (downloads & transcribes automatically)
- View the **transcribed text** and **download it**  

---

## Project Structure

```mint
app
├── __init__.py
├── api
│   ├── __init__.py
│   ├── router.py
├── config.py
├── main.py
├── models
│   ├── __init__.py
├── services
│   ├── __init__.py
│   ├── downloader.py
│   ├── file_manager.py
│   ├── transcriber.py
└── utils
    ├── __init__.py
    ├── file_utils.py
```

---

## Technologies Used

| Tool          | Purpose |
|--------------|---------|
| **FastAPI**  | Backend API |
| **Streamlit** | Frontend UI |
| **yt-dlp**   | YouTube Downloading |
| **Whisper**  | Speech-to-Text |
| **FFmpeg**   | Audio Processing |
| **Pydantic** | Data Validation |
| **Uvicorn**  | ASGI Server |

---

## License

This project is licensed under the **MIT License**.

---

## 🚀 Enjoy Fast & Accurate YouTube Transcription!

🔹 Made with ❤️ using **FastAPI**, **Streamlit**, **yt-dlp**, & **OpenAI Whisper**.