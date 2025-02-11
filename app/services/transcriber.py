import pathlib
import whisper
from app.config import settings
from app.utils.file_utils import write_text_to_file

# Load Whisper **once** and reuse it
WHISPER_MODEL = whisper.load_model(settings.whisper_model)

def transcribe_audio(audio_path: str) -> str:
    """Transcribes audio using Whisper."""
    if not audio_path or not pathlib.Path(audio_path).exists():
        print("❌ Error: Audio file not found.")
        return ""

    try:
        result = WHISPER_MODEL.transcribe(audio_path)
        write_text_to_file(result["text"], f"{audio_path}.txt")
        return result["text"]
    except Exception as e:
        print(f"❌ Error transcribing audio: {e}")
        return ""
