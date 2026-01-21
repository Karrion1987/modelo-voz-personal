# 🚂 Guía Paso a Paso: Desplegar en Railway

## ✅ Plan Gratuito de Railway

- **$5 de crédito gratis** cada mes
- Suficiente para proyectos pequeños/medianos
- Se renueva automáticamente cada mes
- Si te quedas sin crédito, el servicio se pausa (no se cobra nada)

---

## 📋 Paso a Paso

### Paso 1: Subir Cambios a GitHub (si no lo hiciste)

```bash
git add .
git commit -m "Preparado para Railway"
git push
```

### Paso 2: Crear Cuenta en Railway

1. Ve a https://railway.app
2. Haz clic en **"Start a New Project"**
3. Selecciona **"Login with GitHub"**
4. Autoriza Railway a acceder a tus repositorios

### Paso 3: Crear Nuevo Proyecto

1. En el dashboard de Railway, haz clic en **"New Project"**
2. Selecciona **"Deploy from GitHub repo"**
3. Busca y selecciona tu repositorio `modelo-voz-personal` (o como lo hayas llamado)
4. Railway detectará automáticamente que es Python

### Paso 4: Configurar el Servicio

Railway debería detectar automáticamente:
- ✅ Lenguaje: Python
- ✅ Build Command: `pip install -r requirements.txt`
- ✅ Start Command: `python app.py`

**Si no lo detecta automáticamente:**
1. Haz clic en el servicio
2. Ve a **"Settings"**
3. En **"Build Command"**: `pip install -r requirements.txt`
4. En **"Start Command"**: `python app.py`

### Paso 5: Generar Dominio Público

1. En el servicio, haz clic en **"Settings"**
2. Ve a la sección **"Networking"**
3. Haz clic en **"Generate Domain"**
4. Railway te dará una URL como: `https://modelo-voz-personal-production.up.railway.app`

### Paso 6: Esperar el Despliegue

- Railway empezará a construir tu proyecto (2-3 minutos)
- Verás los logs en tiempo real
- Cuando veas `Uvicorn running on...` está listo

### Paso 7: Probar tu API

Abre la URL que Railway te dio:
- `https://tu-url.railway.app/` → Deberías ver `{"status": "ok", ...}`
- `https://tu-url.railway.app/docs` → Interfaz interactiva de FastAPI

---

## 🧪 Probar desde Otro Proyecto

Ahora puedes usar tu API desde cualquier lugar:

```python
import requests

# Usa tu URL de Railway
API_URL = "https://tu-url.railway.app/transcribe"

with open("audio.ogg", "rb") as f:
    files = {"file": f}
    response = requests.post(API_URL, files=files)
    print(response.json()["text"])
```

---

## ⚙️ Variables de Entorno (Opcional)

Railway maneja automáticamente:
- `PORT` - Se configura automáticamente
- `HOST` - Se configura automáticamente

No necesitas configurar nada más.

---

## 🔍 Ver Logs

1. En Railway, haz clic en tu servicio
2. Ve a la pestaña **"Deployments"**
3. Haz clic en el deployment más reciente
4. Verás los logs en tiempo real

---

## 💰 Monitorear Uso de Créditos

1. Haz clic en tu nombre (arriba a la derecha)
2. Ve a **"Account"**
3. Verás cuántos créditos has usado este mes

---

## 🐛 Solución de Problemas

### Error: "Build failed"
- Verifica que `requirements.txt` esté correcto
- Revisa los logs para ver el error específico

### Error: "Service crashed"
- Revisa los logs en Railway
- Asegúrate de que `app.py` esté en la raíz del proyecto

### La API responde muy lento
- Es normal la primera vez (cold start)
- Railway puede tardar 30-60 segundos en iniciar si no se usa

### Error: "ffmpeg not found"
- Railway debería instalar ffmpeg automáticamente con `nixpacks.toml`
- Si no, verifica que el archivo esté en el repositorio

---

## 📝 Notas Importantes

1. **Primera carga**: La primera vez descargará el modelo Whisper (~72MB), puede tardar
2. **Cold start**: Si no se usa por un tiempo, Railway puede "dormir" el servicio
3. **Límites**: Con el plan gratuito, tienes suficiente para desarrollo y pruebas
4. **Actualizaciones**: Cada vez que hagas `git push`, Railway desplegará automáticamente

---

## 🎯 Siguiente Paso

Una vez desplegado, copia tu URL de Railway y úsala en tus otros proyectos:

```python
API_URL = "https://tu-url.railway.app/transcribe"
```

¡Listo! 🎉
