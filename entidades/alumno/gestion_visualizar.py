import json
from pathlib import Path
from utils import pantalla as headers
from utils import busquedas as busqueda

DATOS_DIR = Path(__file__).resolve().parents[1] / "datos"
CURSOS_JSON = DATOS_DIR / "cursos.json"

def _leer_lista_json(ruta: Path):
    try:
        with ruta.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        return []
    except Exception:
        return []

def verMisCursos(legajo):
    alumno = busqueda.buscarAlumnoPorLegajo(legajo)
    if alumno is None or "cursos" not in alumno or not isinstance(alumno["cursos"], list) or len(alumno["cursos"]) == 0:
        print(headers.Fore.RED + "No estás inscripto en ningún curso.")
        return

    headers.header("MIS CURSOS")
    for par in alumno["cursos"]:
        if isinstance(par, (list, tuple)) and len(par) >= 2:
            idCurso = par[0]
            estado  = par[1]
            curso = busqueda.buscarCursoPorId(idCurso)
            if curso is not None:
                profesor = busqueda.buscarProfesorPorLegajo(curso["profesor"]) if "profesor" in curso else ""
                colorEstado = headers.Fore.GREEN if estado == "Aprobado" else headers.Fore.RED
                linea = (headers.Fore.WHITE
                         + str(curso["id"]) + " - " + curso["nombre"]
                         + " | Aula: " + curso["aula"]
                         + " | Profesor: " + profesor
                         + " | Estado: ")
                print(linea + colorEstado + estado)

def verCursosDisponibles(legajo):
    cursos = _leer_lista_json(CURSOS_JSON)
    if len(cursos) == 0:
        print(headers.Fore.RED + "No hay cursos disponibles.")
        return

    headers.header("CURSOS DISPONIBLES")
    for curso in cursos:
        if "id" in curso and "nombre" in curso:
            profesor = busqueda.buscarProfesorPorLegajo(curso["profesor"]) if "profesor" in curso else ""
            inscripto = ""
            if "alumnos" in curso and isinstance(curso["alumnos"], list) and legajo in curso["alumnos"]:
                inscripto = headers.Fore.GREEN + " (Inscripto)"
            linea = (headers.Fore.WHITE
                     + "ID: " + str(curso["id"])
                     + " - " + curso["nombre"]
                     + " (Profesor: " + profesor + ")")
            print(linea + inscripto)

def verEstadoAprobacion(legajo):
    alumno = busqueda.buscarAlumnoPorLegajo(legajo)
    if alumno is None or "cursos" not in alumno or not isinstance(alumno["cursos"], list) or len(alumno["cursos"]) == 0:
        print(headers.Fore.RED + "No tenés cursos inscriptos.")
        return

    headers.header("ESTADO DE APROBACIÓN")
    for par in alumno["cursos"]:
        if isinstance(par, (list, tuple)) and len(par) >= 2:
            idCurso = par[0]
            estado  = par[1]
            curso = busqueda.buscarCursoPorId(idCurso)
            if curso is not None and "id" in curso and "nombre" in curso:
                colorEstado = headers.Fore.GREEN if estado == "Aprobado" else headers.Fore.RED
                linea = headers.Fore.WHITE + str(curso["id"]) + " - " + curso["nombre"] + " | Estado: "
                print(linea + colorEstado + estado)
