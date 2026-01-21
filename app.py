from pathlib import Path
import os
import tempfile
import shutil

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import whisper


class TranscriptionResponse(BaseModel):
    text: str


app = FastAPI(title="Modelo de voz personal")


def ensure_ffmpeg_on_path() -> None:
    """
    Asegura que la carpeta local de ffmpeg esté en el PATH.
    """
    project_root = Path(__file__).resolve().parent
    ffmpeg_bin = project_root / "ffmpeg" / "ffmpeg-8.0.1-essentials_build" / "bin"
    if ffmpeg_bin.exists():
        path_str = os.environ.get("PATH", "")
        if str(ffmpeg_bin) not in path_str:
            os.environ["PATH"] = f"{ffmpeg_bin}{os.pathsep}{path_str}"


# Inicialización del modelo al arrancar el servidor
ensure_ffmpeg_on_path()
model = whisper.load_model("tiny")


@app.get("/")
def root():
    return {"status": "ok", "message": "Servidor de voz activo. Usa POST /transcribe con un archivo de audio."}


@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Primera prueba: recibe un audio (ogg/wav/mp3) y devuelve solo el texto.
    """
    suffix = Path(file.filename).suffix or ".ogg"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        result = model.transcribe(tmp_path, language="es")
        text = result.get("text", "").strip()
    finally:
        Path(tmp_path).unlink(missing_ok=True)

    return TranscriptionResponse(text=text)


if __name__ == "__main__":
    import uvicorn
    
    # Para producción: usar 0.0.0.0 para que sea accesible desde fuera
    # El puerto puede venir de variable de entorno (Railway, Render, etc.)
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    uvicorn.run("app:app", host=host, port=port, reload=False)

