import json
from database.logica import pathDatos, convertir_lista_tupla
import time

# Se tiene que sacar
# ALUMNOS_DB = []
# PROFESORES_DB = []
# CURSOS_DB = []
# CUOTAS_PENDIENTES = []
# CREDENCIALES = []


def cargar_datos_json():
    """
    Carga los datos de la base de datos en el archivo datos.json, si el archivo no existe, va a retornar un diccionario vacio
    """
    global ALUMNOS_DB, PROFESORES_DB, CURSOS_DB, CUOTAS_PENDIENTES, CREDENCIALES
    try:
        with open(pathDatos, "r") as archivo:
            datos_maestros = json.load(archivo)
            alumnos_convertidos = convertir_lista_tupla(datos_maestros["ALUMNOS_BD"])
            ALUMNOS_DB = alumnos_convertidos
            PROFESORES_DB = datos_maestros.get("PROFESORES_BD")
            CURSOS_DB = datos_maestros.get("CURSOS_BD")
            CUOTAS_PENDIENTES = datos_maestros.get("CUOTAS_PENDIENTES")
            CREDENCIALES = datos_maestros.get("CREDENCIALES")
            print("Datos cargados en la base de datos con exito...")
        time.sleep(2)
        return
    except Exception as e:
        pantalla.redText(e)
        time.sleep(2)
        return


def guardar_datos_json():
    """
    Guarda los datos de la base de datos en el archivo datos.json
    """
    datos_maestro = {
        "ALUMNOS_BD": ALUMNOS_DB,
        "PROFESORES_BD": PROFESORES_DB,
        "CURSOS_BD": CURSOS_DB,
        "CUOTAS_PENDIENTES": CUOTAS_PENDIENTES,
        "CREDENCIALES": CREDENCIALES,
    }
    try:
        with open(pathDatos, "w") as archivo:
            json_maestro = json.dumps(datos_maestro)
            archivo.write(json_maestro)
        print("Datos guardados en la base de datos con exito...")
    except Exception as e:
        print("Error al guardar los datos en la base de datos...")
        print(e)


# con esto inicializamos la base de datos
cargar_datos_json()
