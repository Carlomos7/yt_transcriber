import pathlib
import re
import yt_dlp
import whisper
from config import settings


def sanitize_filename(filename: str) -> str:
    """Sanitize filename by removing special characters."""
    sanitized = re.sub(r"[^a-zA-Z0-9_\-]", "_", filename)
    return sanitized.strip("_")  # Remove leading/trailing underscores


def download_audio_from_youtube(yt_url: str, output_dir: str) -> str:
    """Downloads audio from YouTube and returns the absolute file path."""
    ydl_opts = settings.yt_dlp_options.copy()  # Ensure we don't modify global settings

    try:
        # Ensure output directory exists
        output_path = pathlib.Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Extract video information (dry-run)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(yt_url, download=False)
            title = info_dict.get("title", "audio")
            sanitized_title = sanitize_filename(title)

            # Define the output path (without forcing .mp3)
            ydl_opts["outtmpl"] = str(output_path / sanitized_title)

        # Download the audio with updated options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])

        # `yt-dlp` automatically adds the correct extension (mp3)
        final_path = output_path / f"{sanitized_title}.mp3"

        # Ensure the file exists before returning
        if final_path.exists():
            return str(final_path.resolve())

        print("❌ Error: Download succeeded, but file not found.")
        return None

    except Exception as e:
        print(f"❌ Error downloading audio: {e}")
        return None


# Load Whisper **once** and reuse it
WHISPER_MODEL = whisper.load_model(settings.whisper_model)

def write_text_to_file(text: str, output_path: str) -> None:
    """Write text to a file."""
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print(f"❌ Error writing text to file: {e}")

def transcribe_audio_to_text(audio_path: str) -> str:
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


# Test the function with user input
if __name__ == "__main__":
    yt_url = input("Enter a YouTube URL: ").strip()
    output_dir = settings.output_dir or "downloads"

    audio_path = download_audio_from_youtube(yt_url, output_dir)
    if audio_path:
        transcribed_text = transcribe_audio_to_text(audio_path)

        # Pretty-print the transcribed text
        print("\n📜 **Transcribed Text:**\n")
        print(transcribed_text)
    else:
        print("❌ Download failed, no transcription performed.")
