"""
Ejemplo de cómo usar la API de transcripción desde otro proyecto Python.
"""
import requests
from pathlib import Path

# URL de tu API (ajusta según donde esté corriendo)
API_URL = "http://127.0.0.1:8000/transcribe"


def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe un archivo de audio usando la API.
    
    Args:
        audio_path: Ruta al archivo de audio
        
    Returns:
        Texto transcrito
    """
    with open(audio_path, "rb") as f:
        files = {"file": (Path(audio_path).name, f, "audio/ogg")}
        response = requests.post(API_URL, files=files)
        response.raise_for_status()
        return response.json()["text"]


if __name__ == "__main__":
    # Ejemplo de uso
    audio_file = "data/whatsapp/WhatsApp Ptt 2025-07-30 at 11.45.33 AM.ogg"
    
    if Path(audio_file).exists():
        print(f"Transcribiendo {audio_file}...")
        text = transcribe_audio(audio_file)
        print(f"\nTexto transcrito:\n{text}")
    else:
        print(f"Archivo no encontrado: {audio_file}")
        print("\nUso:")
        print("  python example_usage.py")
