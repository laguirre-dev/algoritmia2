import json
from pathlib import Path
from utils import pantalla as headers

DATOS_DIR = Path(__file__).resolve().parents[1] / "BaseDeDatos"
ALUMNOS_JSON = DATOS_DIR / "alumnos.json"
CURSOS_JSON = DATOS_DIR / "cursos.json"

def leerListaJson(ruta: Path):
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

def escribirListaJson(ruta: Path, data):
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(headers.Fore.RED + "[ERROR IO] " + str(e))
        return False

def buscarAlumno(alumnos, legajo):
    for a in alumnos:
        if "legajo" in a and a["legajo"] == legajo:
            return a
    return None

def buscarCurso(cursos, idCursoStr):
    for c in cursos:
        if "id" in c and str(c["id"]).upper() == idCursoStr:
            return c
    return None

def inscribirEnCurso(legajo, idCurso):
    idCursoStr = str(idCurso).upper()

    alumnos = leerListaJson(ALUMNOS_JSON)
    cursos = leerListaJson(CURSOS_JSON)

    alumno = buscarAlumno(alumnos, legajo)
    if alumno is None:
        print(headers.Fore.RED + "Alumno inexistente.")
        return False

    curso = buscarCurso(cursos, idCursoStr)
    if curso is None:
        print(headers.Fore.RED + "Curso inexistente.")
        return False

    if "cursos" not in alumno or not isinstance(alumno["cursos"], list):
        alumno["cursos"] = []

    yaInscripto = False
    for par in alumno["cursos"]:
        if isinstance(par, (list, tuple)) and len(par) >= 1 and str(par[0]).upper() == idCursoStr:
            yaInscripto = True
            break

    if yaInscripto:
        print(headers.Fore.RED + "Ya estás inscripto en ese curso.")
        return False

    alumno["cursos"].append([idCursoStr, "Desaprobado"])

    if "alumnos" not in curso or not isinstance(curso["alumnos"], list):
        curso["alumnos"] = []
    if legajo not in curso["alumnos"]:
        curso["alumnos"].append(legajo)
        try:
            curso["alumnos"].sort()
        except:
            pass

    ok1 = escribirListaJson(ALUMNOS_JSON, alumnos)
    ok2 = escribirListaJson(CURSOS_JSON, cursos)
    if not (ok1 and ok2):
        return False

    nombreCurso = curso["nombre"] if "nombre" in curso else idCursoStr
    print(headers.Fore.GREEN + "Inscripción exitosa a " + nombreCurso + ".")
    return True

def darseDeBaja(legajo, idCurso):
    idCursoStr = str(idCurso).upper()

    alumnos = leerListaJson(ALUMNOS_JSON)
    cursos = leerListaJson(CURSOS_JSON)

    alumno = buscarAlumno(alumnos, legajo)
    if alumno is None:
        print(headers.Fore.RED + "Alumno inexistente.")
        return False

    curso = buscarCurso(cursos, idCursoStr)
    if curso is None:
        print(headers.Fore.RED + "Curso inexistente.")
        return False

    if "cursos" not in alumno or not isinstance(alumno["cursos"], list):
        alumno["cursos"] = []

    estaba = False
    nuevaLista = []
    for par in alumno["cursos"]:
        if isinstance(par, (list, tuple)) and len(par) >= 1 and str(par[0]).upper() == idCursoStr:
            estaba = True
        else:
            nuevaLista.append(par)

    if not estaba:
        print(headers.Fore.RED + "No estabas inscripto en ese curso.")
        return False

    alumno["cursos"] = nuevaLista

    if "alumnos" in curso and isinstance(curso["alumnos"], list):
        curso["alumnos"] = [l for l in curso["alumnos"] if l != legajo]

    ok1 = escribirListaJson(ALUMNOS_JSON, alumnos)
    ok2 = escribirListaJson(CURSOS_JSON, cursos)
    if not (ok1 and ok2):
        return False

    nombreCurso = curso["nombre"] if "nombre" in curso else idCursoStr
    print(headers.Fore.GREEN + "Baja exitosa de " + nombreCurso + ".")
    return True
