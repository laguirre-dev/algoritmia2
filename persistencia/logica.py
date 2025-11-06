import json

def cargar_datos_json():
    """
    Carga los datos de la base de datos en el archivo datos.json, si el archivo no existe, va a retornar un diccionario vacio
    """
    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:
            datos_maestros = json.load(archivo)
        print("Datos cargados con exito...")
        return (
            datos_maestros.get("ALUMONS_BD", []),
            datos_maestros.get("PROFESORES_BD", []),
            datos_maestros.get("CURSOS_BD", []),
            datos_maestros.get("PAGOS_PENDIENTES", []),
            datos_maestros.get("CREDENCIALES", []),
        )
    except FileNotFoundError:
        print("Archivo no encontrado, se crearon bases de datos vacias...")
        return ([], [], [], [], [])
    except json.JSONDecodeError:
        print("Error al traer los datos del json, el archivo esta dañado")
        return ([], [], [], [], [])
    
def guardar_datos_json(alumnos, profesores, cursos, pagos_pendientes, credenciales):
    """
    Guarda los datos de la base de datos en el archivo datos.json
    """
    datos_maestro = {
        "ALUMNOS_BD": alumnos,
        "PROFESORES_BD": profesores,
        "CURSOS_BD": cursos,
        "PAGOS_PENDIENTES": pagos_pendientes,
        "CREDENCIALES": credenciales
    }
    try:
        with open("datos.json", "w", encoding="utf-8") as archivo:
            json.dump(datos_maestro, archivo, indent=4, ensure_ascii=False) 
        print("Datos guardados en la base de datos con exito...")
    except IOError:
        print("Error al guardar los datos en la base de datos...")