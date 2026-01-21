from setuptools import setup, find_packages
from pathlib import Path

# Leer README para la descripción larga
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="modelo-voz-personal",
    version="1.0.0",
    description="API REST para transcripción de voz usando Whisper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tu Nombre",
    author_email="tu@email.com",
    url="https://github.com/tu-usuario/modelo-voz-personal",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.128.0",
        "uvicorn>=0.40.0",
        "openai-whisper>=20250625",
        "pydantic>=2.12.5",
    ],
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    entry_points={
        "console_scripts": [
            "modelo-voz=app:main",
        ],
    },
)
