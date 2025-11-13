import os
import json
from utils import pantalla as headers

RUTA_REPORTES = os.path.join(os.path.dirname(__file__), "archivos")

if not os.path.exists(RUTA_REPORTES):
    os.makedirs(RUTA_REPORTES)

def guardarReporte(nombre_archivo, contenido):
    """
    Guarda un reporte en la carpeta de reportes.
    - nombre_archivo: nombre base del archivo (sin extensión)
    - contenido: lista de diccionarios con los datos
    """
    try:
        ruta = os.path.join(RUTA_REPORTES, f"{nombre_archivo}.txt")
        with open(ruta, "w") as f:
            for item in contenido:
                linea = " | ".join([f"{k}: {v}" for k, v in item.items()])
                f.write(linea + "\n")
        print(headers.Fore.GREEN + f"Reporte guardado en {ruta}")
    except Exception as e:
        print(headers.Fore.RED + f"Error al guardar reporte: {e}")

def listarReportes():
    """
    Lista todos los reportes generados en la carpeta.
    """
    try:
        archivos = os.listdir(RUTA_REPORTES)
        if not archivos:
            print(headers.Fore.YELLOW + "No hay reportes generados aún.")
            return
        headers.header("REPORTES DISPONIBLES")
        for archivo in archivos:
            print(headers.Fore.WHITE + f"- {archivo}")
    except Exception as e:
        print(headers.Fore.RED + f"Error al listar reportes: {e}")