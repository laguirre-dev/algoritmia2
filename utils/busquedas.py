import json
from pathlib import Path
from . import pantalla as headers

DATOS_DIR = Path(__file__).resolve().parents[1] / "baseDeDatos"

ALUMNOS_JSON     = DATOS_DIR / "alumnos.json"
PROFESORES_JSON  = DATOS_DIR / "profesores.json"
CURSOS_JSON      = DATOS_DIR / "cursos.json"
CUOTAS_JSON      = DATOS_DIR / "cuotas_pendientes.json"


# ---------------------------
# Lectura básica de JSON
# ---------------------------
def _leer_lista_json(ruta: Path):
    """
    Intenta leer una lista desde un archivo JSON.
    Si no existe o hay error, devuelve [].
    """
    try:
        with ruta.open("r", encoding="utf-8") as f:
            data = json.load(f)
            # Si por alguna razón no es lista, devuelvo lista vacía.
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except Exception:
        # Cualquier otro error de lectura/parseo
        return []


# ---------------------------
# Búsquedas
# ---------------------------
def buscarAlumnoPorLegajo(legajo):
    """
    Busca un alumno por legajo. Devuelve el dict del alumno o None.
    """
    alumnos = _leer_lista_json(ALUMNOS_JSON)
    for alumno in alumnos:
        # Se asume que el JSON tiene la clave "legajo"
        if "legajo" in alumno and alumno["legajo"] == legajo:
            return alumno
    return None


def buscarAlumnoPorLegajoNombreYApellido(legajo):
    """
    Devuelve 'Nombre Apellido' o un mensaje si no existe.
    """
    alumno = buscarAlumnoPorLegajo(legajo)
    if alumno is not None:
        nombre = alumno["nombre"] if "nombre" in alumno else ""
        apellido = alumno["apellido"] if "apellido" in alumno else ""
        completo = (nombre + " " + apellido).strip()
        if completo != "":
            return completo
        else:
            return "Alumno #" + str(legajo)
    return "Alumno con legajo " + str(legajo) + " no encontrado"


def buscarProfesorPorLegajo(legajo_profesor):
    """
    Busca un profesor por legajo. Devuelve 'Nombre Apellido' o mensaje si no existe.
    """
    profesores = _leer_lista_json(PROFESORES_JSON)
    for profesor in profesores:
        if "legajo" in profesor and profesor["legajo"] == legajo_profesor:
            nombre = profesor["nombre"] if "nombre" in profesor else ""
            apellido = profesor["apellido"] if "apellido" in profesor else ""
            completo = (nombre + " " + apellido).strip()
            if completo != "":
                return completo
            else:
                return "Profesor #" + str(legajo_profesor)
    return "Profesor con legajo " + str(legajo_profesor) + " no encontrado"


def buscarCursoPorId(idCurso):
    """
    Busca un curso por id. Devuelve el dict del curso o None.
    Nota: tus IDs están en mayúsculas en cursos.json (por ejemplo 'AED1').
    Para evitar errores, comparo como string y en mayúsculas.
    """
    cursos = _leer_lista_json(CURSOS_JSON)
    id_normalizado = str(idCurso).upper()
    for curso in cursos:
        if "id" in curso and str(curso["id"]).upper() == id_normalizado:
            return curso
    return None


def validarAlumnoYCurso(legajo, idCurso):
    """
    Devuelve (alumno, curso) o (None, None) e imprime mensaje si falta alguno.
    """
    alumno = buscarAlumnoPorLegajo(legajo)
    curso = buscarCursoPorId(idCurso)
    if alumno is None or curso is None:
        print(headers.Fore.RED + "Alumno o curso inexistente.")
        return None, None
    return alumno, curso


def buscarPagosPendientesPorLegajo(legajo):
    """
    Devuelve lista de cuotas pendientes del alumno.
    Cada ítem es un dict con 'cuota_nro' y 'legajo'.
    """
    cuotas = _leer_lista_json(CUOTAS_JSON)
    resultado = []
    for c in cuotas:
        if "legajo" in c and c["legajo"] == legajo:
            resultado.append(c)
    return resultado


# Placeholders para compatibilidad (si alguien los llama)
def buscar_materia():
    print("En desarrollo...")
    return None

def buscar_pagos():
    print("En desarrollo...")
    return None
