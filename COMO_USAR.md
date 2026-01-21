# 🚀 Cómo Usar el Proyecto desde GitHub

## Opción 1: Clonar y Usar Localmente

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
```

### Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Nota**: La primera vez descargará el modelo Whisper (unos 72MB), puede tardar unos minutos.

### Paso 3: Ejecutar el Servidor

**Windows:**
```bash
python app.py
```

O usa el script:
```bash
start_server.bat
```

**Linux/Mac:**
```bash
python3 app.py
```

O:
```bash
bash start_server.sh
```

### Paso 4: Probar la API

El servidor estará en `http://127.0.0.1:8000`

- **Interfaz web**: Abre `http://127.0.0.1:8000/docs` en tu navegador
- **Probar endpoint**: `http://127.0.0.1:8000/`

---

## Opción 2: Desplegar como Servicio (URL Pública)

### 🚂 Railway (Recomendado - Más Fácil)

1. Ve a https://railway.app y crea una cuenta (puedes usar GitHub)
2. Haz clic en **"New Project"** → **"Deploy from GitHub repo"**
3. Selecciona tu repositorio `modelo-voz-personal`
4. Railway detectará automáticamente que es Python/FastAPI
5. Espera a que termine el despliegue (2-3 minutos)
6. Haz clic en el servicio → **"Settings"** → **"Generate Domain"**
7. ¡Listo! Tendrás una URL pública como: `https://tu-api.railway.app`

**Configuración adicional en Railway:**
- En "Variables" agrega si es necesario:
  - `PORT=8000` (Railway lo maneja automáticamente)

### 🌐 Render

1. Ve a https://render.com y crea una cuenta
2. Haz clic en **"New +"** → **"Web Service"**
3. Conecta tu repositorio de GitHub
4. Configuración:
   - **Name**: `modelo-voz-personal`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. Haz clic en **"Create Web Service"**
6. Espera el despliegue (3-5 minutos)
7. Obtendrás una URL como: `https://modelo-voz-personal.onrender.com`

**Nota**: Render puede tardar en iniciar la primera vez (cold start).

### 🐳 Docker (Avanzado)

Si prefieres usar Docker:

```bash
docker build -t modelo-voz .
docker run -p 8000:8000 modelo-voz
```

---

## Opción 3: Usar desde Otros Proyectos

### Como API Local

Si tienes el servidor corriendo en `http://localhost:8000`:

**Python:**
```python
import requests

url = "http://localhost:8000/transcribe"
with open("audio.ogg", "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)
    texto = response.json()["text"]
    print(texto)
```

**JavaScript/Node.js:**
```javascript
const FormData = require('form-data');
const fs = require('fs');
const axios = require('axios');

const form = new FormData();
form.append('file', fs.createReadStream('audio.ogg'));

axios.post('http://localhost:8000/transcribe', form, {
  headers: form.getHeaders()
})
.then(response => console.log(response.data.text))
.catch(error => console.error(error));
```

**cURL:**
```bash
curl -X POST "http://localhost:8000/transcribe" \
  -F "file=@audio.ogg"
```

### Como API Remota (Railway/Render)

Solo cambia la URL:

```python
# En lugar de localhost, usa tu URL de Railway/Render
url = "https://tu-api.railway.app/transcribe"
```

---

## 🔧 Solución de Problemas

### Error: "ffmpeg not found"

**Windows**: El proyecto incluye ffmpeg portable, debería funcionar automáticamente.

**Linux/Mac**: Instala ffmpeg:
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Mac
brew install ffmpeg
```

### Error: "Port already in use"

Cambia el puerto en `app.py`:
```python
uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=False)
```

### Error: "CUDA out of memory" o muy lento

Usa un modelo más pequeño en `app.py`:
```python
model = whisper.load_model("tiny")  # En lugar de "base" o "small"
```

### El modelo tarda mucho en cargar

Es normal la primera vez. El modelo se descarga y cachea en `~/.cache/whisper/`

---

## 📝 Notas Importantes

1. **Primera ejecución**: Descargará el modelo Whisper (~72MB para "tiny")
2. **Memoria**: El modelo "tiny" usa ~1GB de RAM
3. **Velocidad**: "tiny" es rápido pero menos preciso que "base" o "small"
4. **Producción**: Para producción, considera usar un modelo más grande o GPU

---

## 🎯 Próximos Pasos

1. ✅ Clona el proyecto
2. ✅ Instala dependencias
3. ✅ Ejecuta el servidor
4. ✅ Prueba con `http://localhost:8000/docs`
5. ✅ Despliega en Railway/Render para tener URL pública
6. ✅ Usa la URL pública en tus otros proyectos
