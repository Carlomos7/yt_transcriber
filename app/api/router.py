from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.responses import FileResponse
from app.models import DownloadRequest, TranscribeRequest, FileRequest
from app.services.downloader import download_audio_from_youtube, download_video_from_youtube
from app.services.transcriber import transcribe_audio
from app.services.file_manager import get_file_path

router = APIRouter()

### **🔹 Download Routes**
@router.post("/download/audio/")
async def download_audio(request: DownloadRequest):
    """Download YouTube audio."""
    audio_path = download_audio_from_youtube(request.url, request.output_dir)

    if not audio_path:
        raise HTTPException(status_code=500, detail="Failed to download audio.")

    return {"message": "Download successful", "file_path": audio_path}

@router.post("/download/video/")
async def download_video(request: DownloadRequest):
    """Download YouTube video."""
    video_path = download_video_from_youtube(request.url, request.output_dir)

    if not video_path:
        raise HTTPException(status_code=500, detail="Failed to download video.")

    return {"message": "Download successful", "file_path": video_path}


### **🔹 Transcription Routes**
@router.post("/transcribe/")
async def transcribe_audio(request: TranscribeRequest):
    """Transcribe an audio file."""
    transcription = transcribe_audio(request.file_path)

    if not transcription:
        raise HTTPException(status_code=500, detail="Failed to transcribe audio.")

    return {"transcription": transcription}


### **🔹 File Retrieval Routes**
@router.get("/files/audio/{filename}")
async def get_audio_file(filename: str):
    """Retrieve a downloaded audio file."""
    file_path = get_file_path("audio", filename)
    if not file_path:
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(file_path, media_type="audio/mpeg", filename=filename)


@router.get("/files/video/{filename}")
async def get_video_file(filename: str):
    """Retrieve a downloaded video file."""
    file_path = get_file_path("video", filename)
    if not file_path:
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(file_path, media_type="video/mp4", filename=filename)


@router.get("/files/text/{filename}")
async def get_text_file(filename: str):
    """Retrieve a saved transcription file."""
    file_path = get_file_path("text", filename)
    if not file_path:
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(file_path, media_type="text/plain", filename=filename)