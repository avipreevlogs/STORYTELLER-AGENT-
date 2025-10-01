import os
import sys
from pathlib import Path

def detect_ffmpeg():
    ffmpeg_path = Path("ffmpeg.exe")
    if ffmpeg_path.exists():
        return str(ffmpeg_path)
    return "ffmpeg"  # Assume system-installed

def main():
    api_key = os.getenv("OPENAI_API_KEY", "MISSING_KEY")
    client_secret = os.getenv("CLIENT_SECRET_JSON", "MISSING_SECRET")

    print("=== Storytelling Agent ===")
    print(f"Using OpenAI API Key: {'SET' if api_key != 'MISSING_KEY' else 'NOT SET'}")
    print(f"Using Google Client Secret: {'SET' if client_secret != 'MISSING_SECRET' else 'NOT SET'}")

    # Example placeholder logic
    print("Generating story...")
    print("Adding background music...")
    print("Creating video...")
    print("Uploading to YouTube... (placeholder)")

if __name__ == "__main__":
    main()
