# 🔌 Cómo Usar la API desde Otros Proyectos

## Opción 1: API Local (Más Rápido)

### Paso 1: Iniciar tu API

En la carpeta del proyecto de voz (`Modelo de audio IA`):

```bash
python app.py
```

Verás: `Uvicorn running on http://0.0.0.0:8000`

### Paso 2: Usar desde otro proyecto Python

En tu otro proyecto, simplemente llama a la API:

```python
import requests

# URL de tu API local
API_URL = "http://localhost:8000/transcribe"

# Enviar audio
with open("mi_audio.ogg", "rb") as f:
    files = {"file": f}
    response = requests.post(API_URL, files=files)
    
texto_transcrito = response.json()["text"]
print(texto_transcrito)
```

### Paso 3: Usar desde JavaScript/Node.js

```javascript
const FormData = require('form-data');
const fs = require('fs');
const axios = require('axios');

const form = new FormData();
form.append('file', fs.createReadStream('audio.ogg'));

axios.post('http://localhost:8000/transcribe', form, {
  headers: form.getHeaders()
})
.then(response => {
  console.log('Texto:', response.data.text);
})
.catch(error => console.error('Error:', error));
```

### Paso 4: Usar desde cURL (terminal)

```bash
curl -X POST "http://localhost:8000/transcribe" \
  -F "file=@audio.ogg"
```

---

## Opción 2: API Pública (Railway/Render)

Si quieres una URL pública para usar desde cualquier lugar:

### Desplegar en Railway (5 minutos)

1. Ve a https://railway.app
2. Login con GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Selecciona tu repo `modelo-voz-personal`
5. Espera 2-3 minutos
6. Settings → Generate Domain
7. Obtienes: `https://tu-api.railway.app`

### Usar la URL pública

Solo cambia la URL en tu código:

```python
# En lugar de localhost, usa tu URL de Railway
API_URL = "https://tu-api.railway.app/transcribe"

response = requests.post(API_URL, files={"file": open("audio.ogg", "rb")})
print(response.json()["text"])
```

---

## 📝 Ejemplo Completo: Cliente Python

Crea un archivo `cliente_voz.py` en tu otro proyecto:

```python
import requests
from pathlib import Path

class ClienteVozAPI:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
    
    def transcribir(self, audio_path: str) -> str:
        """
        Transcribe un archivo de audio.
        
        Args:
            audio_path: Ruta al archivo de audio
            
        Returns:
            Texto transcrito
        """
        url = f"{self.base_url}/transcribe"
        
        with open(audio_path, "rb") as f:
            files = {"file": (Path(audio_path).name, f)}
            response = requests.post(url, files=files)
            response.raise_for_status()
            return response.json()["text"]
    
    def saludar(self) -> dict:
        """Verifica que la API esté funcionando"""
        response = requests.get(f"{self.base_url}/")
        return response.json()


# Uso
if __name__ == "__main__":
    # Para API local
    cliente = ClienteVozAPI("http://localhost:8000")
    
    # Para API pública (Railway)
    # cliente = ClienteVozAPI("https://tu-api.railway.app")
    
    # Verificar conexión
    print(cliente.saludar())
    
    # Transcribir
    texto = cliente.transcribir("audio.ogg")
    print(f"Transcripción: {texto}")
```

---

## 🎯 Resumen Rápido

**Para usar localmente:**
1. Ejecuta `python app.py` en el proyecto de voz
2. En tu otro proyecto: `requests.post("http://localhost:8000/transcribe", files={"file": ...})`

**Para usar desde cualquier lugar:**
1. Despliega en Railway (5 min)
2. Usa la URL pública: `requests.post("https://tu-api.railway.app/transcribe", ...)`

---

## ⚠️ Notas Importantes

- **API debe estar corriendo**: Asegúrate de que `python app.py` esté ejecutándose
- **Mismo formato**: La API acepta `.ogg`, `.wav`, `.mp3`, `.m4a`
- **Timeout**: Para audios largos, considera aumentar el timeout:
  ```python
  response = requests.post(url, files=files, timeout=300)  # 5 minutos
  ```
