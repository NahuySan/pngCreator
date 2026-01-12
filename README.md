# pngCreator

Script de automatización en Python para la conversión masiva de imágenes a formato PNG directamente desde el Explorador de Archivos de Windows mediante un atajo de teclado global.

Lo hice con la idea de optimizar flujos de trabajo en diseño y desarrollo web, permitiendo procesar múltiples archivos sin abrir software extra.

## Características

* **Hotkey Global**: Ejecución mediante la combinación `Ctrl + Shift + C`.
* **Selección Múltiple**: Capacidad para procesar todos los archivos seleccionados en la ventana activa del Explorador.
* **Formatos Soportados**: Convierte automáticamente archivos `.jpg`, `.jpeg` y `.webp`.
* **Notificaciones Nativas**: Avisos a través del sistema de notificaciones de Windows al finalizar el proceso.
* **Ejecución Silenciosa**: Configurado para correr en segundo plano sin ventanas de terminal (usando `pythonw`).

## Requisitos Técnico

* **Python 3.10+**
* **Librerías**:
    * `Pillow`: Procesamiento de imágenes.
    * `keyboard`: Captura de eventos de teclado.
    * `pywin32`: Interacción con el API de Windows (COM).
    * `plyer`: Notificaciones de escritorio.
