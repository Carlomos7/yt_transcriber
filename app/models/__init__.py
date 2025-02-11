from pydantic import BaseModel

class DownloadRequest(BaseModel):
    """Model for handling YouTube download requests."""
    url: str
    output_dir: str = "downloads"

class TranscribeRequest(BaseModel):
    """Model for handling transcription requests."""
    file_path: str

class FileRequest(BaseModel):
    """Model for handling file retrieval requests."""
    filename: str