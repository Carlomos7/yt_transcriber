import re

def sanitize_filename(filename: str) -> str:
    """Sanitize filename by removing special characters."""
    sanitized = re.sub(r"[^a-zA-Z0-9_\-]", "_", filename)
    return sanitized.strip("_")

def write_text_to_file(text: str, output_path: str) -> None:
    """Write text to a file."""
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print(f"❌ Error writing text to file: {e}")
