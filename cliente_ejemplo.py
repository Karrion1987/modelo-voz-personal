"""
Ejemplo simple para copiar y usar en tu otro proyecto.
Solo necesitas tener 'requests' instalado: pip install requests
"""
import requests

# ============================================
# CONFIGURACIÓN: Cambia esto según tu caso
# ============================================

# Opción 1: Si la API está corriendo localmente
API_URL = "http://localhost:8000/transcribe"

# Opción 2: Si la desplegaste en Railway/Render (descomenta y usa tu URL)
# API_URL = "https://tu-api.railway.app/transcribe"


def transcribir_audio(ruta_audio: str) -> str:
    """
    Transcribe un archivo de audio usando tu API de voz.
    
    Args:
        ruta_audio: Ruta al archivo de audio (.ogg, .wav, .mp3, etc.)
        
    Returns:
        Texto transcrito del audio
    """
    with open(ruta_audio, "rb") as archivo:
        files = {"file": archivo}
        respuesta = requests.post(API_URL, files=files)
        respuesta.raise_for_status()  # Lanza error si algo falla
        return respuesta.json()["text"]


# ============================================
# EJEMPLO DE USO
# ============================================

if __name__ == "__main__":
    # 1. Asegúrate de que tu API esté corriendo (python app.py)
    
    # 2. Usa la función
    try:
        texto = transcribir_audio("mi_audio.ogg")
        print(f"Texto transcrito: {texto}")
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar a la API")
        print("   Asegúrate de ejecutar: python app.py")
    except FileNotFoundError:
        print("❌ Error: Archivo de audio no encontrado")
    except Exception as e:
        print(f"❌ Error: {e}")
