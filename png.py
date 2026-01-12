import os
import keyboard
from PIL import Image
import pythoncom
import win32com.client
# ... tus otros imports
from plyer import notification

def notificar(titulo, mensaje):
    """Lanza una notificación nativa en Windows."""
    notification.notify(
        title=titulo,
        message=mensaje,
        app_name='ImageConverter',
        timeout=3  # Segundos que dura el globo en pantalla
    )


def get_selected_paths(): # Lo pasamos a plural
    pythoncom.CoInitialize()
    paths = []
    try:
        shell = win32com.client.Dispatch("Shell.Application")
        for window in shell.Windows():
            if "explorer.exe" in window.FullName.lower():
                selected_items = window.Document.SelectedItems()
                for item in selected_items:
                    paths.append(item.Path) # Guardamos todos los seleccionados
        return paths
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pythoncom.CoUninitialize()
    return []

def convert_to_png():
    paths = get_selected_paths()
    
    if not paths:
        return

    procesados = 0
    for path in paths:
        nombre_base, ext = os.path.splitext(path)
        ext = ext.lower()

        if ext in ['.jpg', '.jpeg', '.webp']:
            try:
                with Image.open(path) as img:
                    # Si la imagen es RGBA y querés PNG, mantenés el alfa. 
                    # Si es RGB, lo guarda directo.
                    img.save(f"{nombre_base}.png", "PNG")
                procesados += 1
            except Exception as e:
                print(f"Error procesando {path}: {e}")
    
    if procesados > 0:
        notificar("Conversión completada", f"Se convirtieron {procesados} imágenes a PNG.")

# Configuración: Ctrl + Shift + C
HOTKEY = 'ctrl+shift+c'

print(f"Escuchando: {HOTKEY}")
keyboard.add_hotkey(HOTKEY, convert_to_png)

keyboard.wait()