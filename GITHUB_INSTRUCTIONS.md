# Instrucciones para Subir a GitHub

## ✅ Paso 1: Crear el Repositorio en GitHub

1. Ve a https://github.com/new
2. **Nombre del repositorio**: `modelo-voz-personal` (o el nombre que prefieras)
3. **Descripción**: "API REST para transcripción de voz usando Whisper"
4. **Visibilidad**: 
   - ✅ **Público** (si quieres compartirlo)
   - ✅ **Privado** (si solo lo quieres para ti)
5. **NO marques** "Add a README file" (ya tienes uno)
6. **NO marques** "Add .gitignore" (ya tienes uno)
7. Haz clic en **"Create repository"**

## ✅ Paso 2: Conectar tu Repositorio Local con GitHub

Después de crear el repositorio en GitHub, copia la URL que te muestra (algo como):
```
https://github.com/TU-USUARIO/modelo-voz-personal.git
```

Luego ejecuta estos comandos en tu terminal (reemplaza `TU-USUARIO` y `modelo-voz-personal` con tus valores):

```powershell
cd "c:\Users\allan\OneDrive\Escritorio\proyectos\Proyectos\Modelo de audio IA"

# Conectar con GitHub
git remote add origin https://github.com/TU-USUARIO/modelo-voz-personal.git

# Cambiar a rama main (si es necesario)
git branch -M main

# Subir el código
git push -u origin main
```

## ✅ Paso 3: Verificar

Ve a tu repositorio en GitHub y deberías ver todos tus archivos subidos.

## 🔄 Para Futuros Cambios

Cada vez que hagas cambios y quieras subirlos:

```powershell
git add .
git commit -m "Descripción de los cambios"
git push
```

## 📝 Nota sobre Archivos Grandes

Si GitHub te advierte sobre archivos grandes (como los ejecutables de ffmpeg), puedes:

1. **Opción 1**: Usar Git LFS (Large File Storage)
   ```powershell
   git lfs install
   git lfs track "*.exe"
   git add .gitattributes
   git commit -m "Add Git LFS tracking"
   git push
   ```

2. **Opción 2**: Excluir ffmpeg del repositorio (recomendado si es muy grande)
   - Edita `.gitignore` y agrega: `ffmpeg/`
   - Los usuarios pueden descargar ffmpeg por su cuenta

## 🌐 Usar en Otros Proyectos

Una vez subido, otros proyectos pueden clonarlo:

```bash
git clone https://github.com/TU-USUARIO/modelo-voz-personal.git
cd modelo-voz-personal
pip install -r requirements.txt
python app.py
```

O usar la API directamente si la despliegas en Railway/Render.
