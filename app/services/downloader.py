import pathlib
import yt_dlp
from app.config import settings
from app.utils.file_utils import sanitize_filename

def download_audio_from_youtube(yt_url: str, output_dir: str) -> str:
    """Downloads YouTube audio and returns file path."""
    return _download_from_youtube(yt_url, output_dir, audio_only=True)

def download_video_from_youtube(yt_url: str, output_dir: str) -> str:
    """Downloads YouTube video and returns file path."""
    return _download_from_youtube(yt_url, output_dir, audio_only=False)

def _download_from_youtube(yt_url: str, output_dir: str, audio_only: bool) -> str:
    """Downloads YouTube content (audio or video)."""
    ydl_opts = settings.yt_dlp_options.copy()
    ydl_opts["format"] = "bestaudio/best" if audio_only else "bestvideo+bestaudio"

    try:
        output_path = pathlib.Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(yt_url, download=False)
            title = sanitize_filename(info_dict.get("title", "video"))
            ydl_opts["outtmpl"] = str(output_path / title)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])

        final_path = output_path / (f"{title}.mp3" if audio_only else f"{title}.mp4")
        return str(final_path.resolve()) if final_path.exists() else None

    except Exception as e:
        print(f"❌ Error downloading: {e}")
        return None
