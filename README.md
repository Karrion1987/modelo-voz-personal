# Modelo de Voz Personal - API de Transcripción

API REST construida con FastAPI que utiliza Whisper para transcribir audios a texto en español. Incluye ffmpeg portable para Windows.

## 🚀 Instalación Rápida

### Requisitos
- Python 3.11 o superior
- Windows/Linux/Mac (ffmpeg incluido para Windows, instalar en Linux/Mac)

### Pasos

1. **Clonar el proyecto desde GitHub**
```bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Ejecutar el servidor**
```bash
python app.py
```

El servidor estará disponible en `http://127.0.0.1:8000`

📖 **Guías detalladas:**
- `QUICK_START.md` - Inicio rápido
- `COMO_USAR.md` - Guía completa de uso y despliegue

## 📖 Uso

### Endpoints Disponibles

#### `GET /`
Verifica que el servidor esté funcionando.
```json
{
  "status": "ok",
  "message": "Servidor de voz activo. Usa POST /transcribe con un archivo de audio."
}
```

#### `POST /transcribe`
Transcribe un archivo de audio a texto.

**Parámetros:**
- `file`: Archivo de audio (ogg, wav, mp3, m4a, etc.)

**Respuesta:**
```json
{
  "text": "Texto transcrito del audio..."
}
```

### Ejemplos de Uso

#### Con cURL
```bash
curl -X POST "http://127.0.0.1:8000/transcribe" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@tu_audio.ogg"
```

#### Con Python
```python
import requests

url = "http://127.0.0.1:8000/transcribe"
with open("audio.ogg", "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)
    print(response.json()["text"])
```

#### Con JavaScript/Fetch
```javascript
const formData = new FormData();
formData.append('file', audioFile);

fetch('http://127.0.0.1:8000/transcribe', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data.text));
```

### Interfaz Web Automática
Visita `http://127.0.0.1:8000/docs` para usar la interfaz interactiva de FastAPI (Swagger UI).

## 🔧 Configuración

### Cambiar el Modelo de Whisper
Edita `app.py` línea 32:
```python
model = whisper.load_model("tiny")  # Opciones: tiny, base, small, medium, large
```

**Nota:** Modelos más grandes = mejor precisión pero más lento y más uso de memoria.

### Cambiar Puerto
Edita `app.py` línea 62:
```python
uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=False)
```

## 📁 Estructura del Proyecto

```
Modelo de audio IA/
├── app.py                 # API principal (FastAPI)
├── transcribe.py          # Script para transcribir múltiples archivos
├── requirements.txt       # Dependencias Python
├── README.md              # Este archivo
├── data/
│   ├── whatsapp/         # Audios de ejemplo
│   └── transcriptions.csv # Transcripciones generadas
└── ffmpeg/               # FFmpeg portable (Windows)
```

## 🌐 Dónde Subir el Proyecto

### Opción 1: GitHub (Recomendado)
1. Crea un repositorio en [GitHub](https://github.com)
2. Sube el proyecto:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

**Ventajas:**
- Gratis y público/privado
- Versionado con Git
- Fácil de compartir y clonar
- Puedes usar GitHub Actions para CI/CD

### Opción 2: GitLab
Similar a GitHub, también gratuito y con repositorios privados.

### Opción 3: PyPI (Para instalación con pip)
Si quieres que otros instalen tu API como paquete:
1. Crea `setup.py` o `pyproject.toml`
2. Publica en PyPI: `python -m pip install build twine && python -m build && python -m twine upload dist/*`

### Opción 4: Docker Hub
Empaqueta en Docker para despliegue fácil:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## 🔐 Uso en Otros Proyectos

### Como Servicio Local
1. Clona el repositorio en tu máquina
2. Instala dependencias: `pip install -r requirements.txt`
3. Ejecuta: `python app.py`
4. Desde otros proyectos, llama a `http://localhost:8000/transcribe`

### Como Paquete Python
Si lo subes a PyPI, otros pueden instalar:
```bash
pip install tu-modelo-voz
```

### Como API Remota
Despliega en servicios como:
- **Heroku**: `git push heroku main`
- **Railway**: Conecta tu repo de GitHub
- **Render**: Conecta tu repo y despliega
- **AWS/GCP/Azure**: Usa contenedores Docker

## 📝 Notas

- El modelo `tiny` es rápido pero menos preciso. Para mejor calidad, usa `base` o `small`.
- FFmpeg está incluido para Windows. En Linux/Mac, instala ffmpeg del sistema.
- Los audios se procesan en memoria temporal y se eliminan después.

## 🐛 Troubleshooting

**Error: "ffmpeg not found"**
- Asegúrate de que la carpeta `ffmpeg/ffmpeg-8.0.1-essentials_build/bin` exista
- En Linux/Mac, instala ffmpeg: `sudo apt install ffmpeg` o `brew install ffmpeg`

**Error: "CUDA out of memory"**
- Usa un modelo más pequeño (`tiny` o `base`)
- O procesa audios más cortos

**Puerto 8000 ya en uso**
- Cambia el puerto en `app.py` línea 62

## 📄 Licencia

Este proyecto es de uso personal. Ajusta según tus necesidades.
