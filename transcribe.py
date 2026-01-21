import csv
import os
from pathlib import Path

from faster_whisper import WhisperModel


DATA_DIR = Path("data/whatsapp")
OUTPUT_CSV = Path("data/transcriptions.csv")
MODEL_NAME = "tiny"  # small and fast enough for a quick pass


def ensure_ffmpeg_on_path() -> None:
    """
    Asegura que la carpeta local de ffmpeg esté en el PATH para que Whisper
    pueda encontrar el binario cuando lo invoque por debajo.
    """
    project_root = Path(__file__).resolve().parent
    ffmpeg_bin = project_root / "ffmpeg" / "ffmpeg-8.0.1-essentials_build" / "bin"
    if ffmpeg_bin.exists():
        path_str = os.environ.get("PATH", "")
        if str(ffmpeg_bin) not in path_str:
            os.environ["PATH"] = f"{ffmpeg_bin}{os.pathsep}{path_str}"


def main() -> None:
    ensure_ffmpeg_on_path()

    files = sorted(
        [p for p in DATA_DIR.glob("*.ogg") if p.is_file()],
        key=lambda p: p.name,
    )
    if not files:
        raise SystemExit(f"No audio files found in {DATA_DIR}")

    model = WhisperModel(MODEL_NAME, device="cpu", compute_type="int8")

    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["path", "text"])
        for audio_path in files:
            print(f"Transcribing {audio_path.name} ...")
            segments, _info = model.transcribe(str(audio_path), language="es", beam_size=5)
            text = " ".join(seg.text for seg in segments).strip()
            writer.writerow([str(audio_path), text])

    print(f"Wrote {len(files)} rows to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
