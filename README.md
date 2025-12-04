# 🤖 Discord Gemini Bot

Este es un bot de Discord simple pero poderoso que integra la inteligencia artificial de **Google Gemini** (modelo `gemini-1.5-flash`) para responder mensajes e interactuar con los usuarios en tu servidor.

## 🚀 Características

* Integración con la API de **Google Gemini**.
* Respuestas rápidas utilizando el modelo `gemini-1.5-flash`.
* Comandos de barra (Slash Commands) fáciles de usar.
* Código limpio y estructurado en Python.

## 📋 Requisitos Previos

Antes de empezar, asegúrate de tener instalado:
* [Python 3.10](https://www.python.org/downloads/) o superior.
* Una cuenta en [Discord Developer Portal](https://discord.com/developers/applications) (para el Token).
* Una API Key de [Google AI Studio](https://aistudio.google.com/) (para Gemini).

## 🛠️ Instalación

Sigue estos pasos para ejecutar el bot en tu computadora:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/MasitasIA/Discord-Gemini-Bot.git](https://github.com/MasitasIA/Discord-Gemini-Bot.git)
    cd Discord-Gemini-Bot
    ```

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    # En Windows
    python -m venv venv
    .\venv\Scripts\activate

    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuración

Este proyecto utiliza variables de entorno para mantener seguras tus claves privadas.

1.  Busca el archivo llamado `.env.example` en la carpeta principal.
2.  Crea una copia de ese archivo y renómbralo a `.env` (sin ninguna extensión extra).
3.  Abre el archivo `.env` y pega tus credenciales:

```ini
DISCORD_TOKEN=Pega_aqui_tu_token_de_discord
GOOGLE_API_KEY=Pega_aqui_tu_api_key_de_google
