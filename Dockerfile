FROM python:3.11-slim

# Instalar ffmpeg (necesario para Whisper)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY app.py .
COPY transcribe.py .

# Exponer puerto
EXPOSE 8000

# Comando por defecto
CMD ["python", "app.py"]
