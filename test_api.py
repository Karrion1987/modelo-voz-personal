"""
Script de prueba rápida para verificar que la API funciona.
Ejecuta este script después de iniciar el servidor con: python app.py
"""
import requests
import sys
from pathlib import Path

API_URL = "http://127.0.0.1:8000"


def test_health():
    """Prueba que el servidor esté funcionando"""
    try:
        response = requests.get(f"{API_URL}/")
        if response.status_code == 200:
            print("✅ Servidor funcionando correctamente")
            print(f"   Respuesta: {response.json()}")
            return True
        else:
            print(f"❌ Error: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar al servidor")
        print("   Asegúrate de que el servidor esté corriendo: python app.py")
        return False


def test_transcribe(audio_path: str):
    """Prueba el endpoint de transcripción"""
    if not Path(audio_path).exists():
        print(f"❌ Archivo no encontrado: {audio_path}")
        return False
    
    try:
        print(f"\n📤 Enviando audio: {audio_path}")
        with open(audio_path, "rb") as f:
            files = {"file": (Path(audio_path).name, f)}
            response = requests.post(f"{API_URL}/transcribe", files=files)
        
        if response.status_code == 200:
            texto = response.json()["text"]
            print("✅ Transcripción exitosa")
            print(f"\n📝 Texto transcrito:\n{texto}\n")
            return True
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"   {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    print("🧪 Prueba de API de Transcripción\n")
    
    # Test 1: Health check
    if not test_health():
        sys.exit(1)
    
    # Test 2: Transcripción (si se proporciona un archivo)
    if len(sys.argv) > 1:
        audio_file = sys.argv[1]
        test_transcribe(audio_file)
    else:
        print("\n💡 Para probar transcripción, ejecuta:")
        print("   python test_api.py ruta/al/audio.ogg")
        print("\n   O usa la interfaz web: http://127.0.0.1:8000/docs")
