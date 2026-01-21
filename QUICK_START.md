# ⚡ Inicio Rápido

## 🎯 Opción Más Rápida: Clonar y Ejecutar

```bash
# 1. Clonar
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO

# 2. Instalar
pip install -r requirements.txt

# 3. Ejecutar
python app.py
```

Abre `http://localhost:8000/docs` y prueba la API.

---

## 🌐 Desplegar en Railway (5 minutos)

1. Ve a https://railway.app
2. Login con GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Selecciona tu repo
5. Espera 2-3 minutos
6. Haz clic en el servicio → "Settings" → "Generate Domain"
7. ¡Listo! Usa la URL en tus proyectos

---

## 📞 Usar desde Otros Proyectos

**Python:**
```python
import requests
response = requests.post(
    "http://localhost:8000/transcribe",  # o tu URL de Railway
    files={"file": open("audio.ogg", "rb")}
)
print(response.json()["text"])
```

**JavaScript:**
```javascript
const formData = new FormData();
formData.append('file', audioFile);

fetch('http://localhost:8000/transcribe', {
  method: 'POST',
  body: formData
})
.then(r => r.json())
.then(data => console.log(data.text));
```

---

📖 **Guía completa**: Ver `COMO_USAR.md`
