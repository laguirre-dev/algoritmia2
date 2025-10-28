import json, os
from pathlib import Path
from utils import pantalla as headers

DATOS_DIR = Path(__file__).resolve().parents[1] / "datos"
ALUMNOS_JSON = DATOS_DIR / "alumnos.json"
CURSOS_JSON  = DATOS_DIR / "cursos.json"

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

def _escribir_lista_json(ruta: Path, data):
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(headers.Fore.RED + "[ERROR IO] " + str(e))
        return False

def _buscar_alumno(alumnos, legajo):
    for a in alumnos:
        if "legajo" in a and a["legajo"] == legajo:
            return a
    return None

def _buscar_curso(cursos, id_curso_str):
    for c in cursos:
        if "id" in c and str(c["id"]).upper() == id_curso_str:
            return c
    return None

def inscribirEnCurso(legajo, idCurso):
    # normalizo id a string en mayúsculas (tus JSON usan "AED1", "PROG2", etc.)
    id_curso_str = str(idCurso).upper()

    alumnos = _leer_lista_json(ALUMNOS_JSON)
    cursos  = _leer_lista_json(CURSOS_JSON)

    alumno = _buscar_alumno(alumnos, legajo)
    if alumno is None:
        print(headers.Fore.RED + "Alumno inexistente.")
        return False

    curso = _buscar_curso(cursos, id_curso_str)
    if curso is None:
        print(headers.Fore.RED + "Curso inexistente.")
        return False

    if "cursos" not in alumno or not isinstance(alumno["cursos"], list):
        alumno["cursos"] = []

    # verificar si ya está inscripto (pares como ["AED1","Desaprobado"])
    ya = False
    for par in alumno["cursos"]:
        if isinstance(par, (list, tuple)) and len(par) >= 1 and str(par[0]).upper() == id_curso_str:
            ya = True
            break
    if ya:
        print(headers.Fore.RED + "Error: Ya estás inscripto en ese curso.")
        return False

    # agregar al alumno
    alumno["cursos"].append([id_curso_str, "Desaprobado"])

    # actualizar lista de alumnos del curso (únicos)
    if "alumnos" not in curso or not isinstance(curso["alumnos"], list):
        curso["alumnos"] = []
    if legajo not in curso["alumnos"]:
        curso["alumnos"].append(legajo)
        # ordenar para prolijidad
        try:
            curso["alumnos"].sort()
        except Exception:
            pass

    ok1 = _escribir_lista_json(ALUMNOS_JSON, alumnos)
    ok2 = _escribir_lista_json(CURSOS_JSON,  cursos)
    if not (ok1 and ok2):
        return False

    nombre_curso = curso["nombre"] if "nombre" in curso else id_curso_str
    print(headers.Fore.GREEN + "Inscripción exitosa a " + nombre_curso + ".")
    return True

def darseDeBaja(legajo, idCurso):
    id_curso_str = str(idCurso).upper()

    alumnos = _leer_lista_json(ALUMNOS_JSON)
    cursos  = _leer_lista_json(CURSOS_JSON)

    alumno = _buscar_alumno(alumnos, legajo)
    if alumno is None:
        print(headers.Fore.RED + "Alumno inexistente.")
        return False

    curso = _buscar_curso(cursos, id_curso_str)
    if curso is None:
        print(headers.Fore.RED + "Curso inexistente.")
        return False

    if "cursos" not in alumno or not isinstance(alumno["cursos"], list):
        alumno["cursos"] = []

    estaba = False
    nueva_lista = []
    for par in alumno["cursos"]:
        if isinstance(par, (list, tuple)) and len(par) >= 1 and str(par[0]).upper() == id_curso_str:
            estaba = True
            # lo omitimos (baja)
        else:
            nueva_lista.append(par)
    if not estaba:
        print(headers.Fore.RED + "No estabas inscripto en ese curso.")
        return False
    alumno["cursos"] = nueva_lista

    # quitar legajo del curso
    if "alumnos" in curso and isinstance(curso["alumnos"], list):
        curso["alumnos"] = [l for l in curso["alumnos"] if l != legajo]

    ok1 = _escribir_lista_json(ALUMNOS_JSON, alumnos)
    ok2 = _escribir_lista_json(CURSOS_JSON,  cursos)
    if not (ok1 and ok2):
        return False

    nombre_curso = curso["nombre"] if "nombre" in curso else id_curso_str
    print(headers.Fore.GREEN + "Baja exitosa de " + nombre_curso + ".")
    return True
