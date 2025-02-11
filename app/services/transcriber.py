import pathlib
import whisper
from app.config import settings
from app.utils.file_utils import write_text_to_file

# Load Whisper once and reuse it
WHISPER_MODEL = whisper.load_model(settings.whisper_model)

def transcribe_the_audio(audio_path: str) -> str:
    """Transcribes audio using Whisper and saves to file."""
    if not audio_path or not pathlib.Path(audio_path).exists():
        print("❌ Error: Audio file not found.")
        return ""

    try:
        print(f"🔄 Attempting to transcribe audio: {audio_path}")
        result = WHISPER_MODEL.transcribe(audio_path)
        transcript_path = f"{audio_path}.txt"
        write_text_to_file(result["text"], transcript_path)
        return result["text"]

    except Exception as e:
        print(f"❌ Error transcribing audio: {e}")
        return ""
