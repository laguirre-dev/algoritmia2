import json
import os
import time
from database.logica import convertirListaTupla
from utils import pantalla

# DICCIONARIO MAESTRO (ESTADO DEL SISTEMA)
sistema = {
    "ALUMNOS_BD": [],
    "PROFESORES_BD": [],
    "CURSOS_BD": [],
    "CUOTAS_PENDIENTES": [],
    "CREDENCIALES": [],
    "RUTA_ARCHIVO": None 
}

def cargarDatosJson(ruta_archivo):
    """
    Carga los datos desde un archivo JSON al diccionario maestro 'sistema'.
    """
    sistema["RUTA_ARCHIVO"] = ruta_archivo
    
    if not os.path.exists(ruta_archivo):
        pantalla.red_text(f"El archivo {ruta_archivo} no existe.")
        time.sleep(2)
        return False

    try:
        with open(ruta_archivo, "r") as archivo:
            datos_cargados = json.load(archivo)
            
            sistema["ALUMNOS_BD"] = convertirListaTupla(datos_cargados.get("ALUMNOS_BD", []))
            sistema["PROFESORES_BD"] = datos_cargados.get("PROFESORES_BD", [])
            sistema["CURSOS_BD"] = datos_cargados.get("CURSOS_BD", [])
            sistema["CUOTAS_PENDIENTES"] = datos_cargados.get("CUOTAS_PENDIENTES", [])
            sistema["CREDENCIALES"] = datos_cargados.get("CREDENCIALES", [])
            
            pantalla.yellow_text(f"Base de datos cargada: {os.path.basename(ruta_archivo)}")
            time.sleep(1)
            return True
            
    except Exception as e:
        pantalla.red_text(f"Error crítico al leer el JSON: {e}")
        time.sleep(2)
        return False

def guardarDatosJson():
    """
    Guarda el estado actual del diccionario 'sistema' en el archivo JSON vinculado.
    """
    ruta = sistema["RUTA_ARCHIVO"]
    
    if not ruta:
        pantalla.red_text("Error: No se ha seleccionado una universidad (ruta no definida).")
        return

    datos_para_guardar = {
        "ALUMNOS_BD": sistema["ALUMNOS_BD"],
        "PROFESORES_BD": sistema["PROFESORES_BD"],
        "CURSOS_BD": sistema["CURSOS_BD"],
        "CUOTAS_PENDIENTES": sistema["CUOTAS_PENDIENTES"],
        "CREDENCIALES": sistema["CREDENCIALES"],
    }

    try:
        with open(ruta, "w") as archivo:
            json.dump(datos_para_guardar, archivo, indent=4)
        pantalla.yellow_text("Cambios guardados exitosamente.")
    except Exception as e:
        pantalla.red_text(f"Error al guardar los datos: {e}")
