"""
El objetivo del módulo es centralizar las funciones reutilizables para usarlas en cualquier parte:
1. Buscar alumno
2. Buscar profesor
3. Buscar materia/curso
4. Buscar pagos

Las funciones devuelven el contenido de la entidad filtrada.
"""

import json, os
from pathlib import Path
from . import pantalla as headers

# ---------------------------
# Rutas a JSON (desde utils/)
# ---------------------------
_DEFAULT_DATOS_DIR = Path(__file__).resolve().parents[1] / "entidades" / "datos"
DATOS_DIR = Path(os.getenv("DATA_DIR", _DEFAULT_DATOS_DIR)).resolve()

ALUMNOS_JSON       = DATOS_DIR / "alumnos.json"
PROFESORES_JSON    = DATOS_DIR / "profesores.json"
CURSOS_JSON        = DATOS_DIR / "cursos.json"
CUOTAS_PEND_JSON   = DATOS_DIR / "cuotas_pendientes.json"

# ---------------------------
# Helpers JSON
# ---------------------------
def _leer_json(ruta: Path, default):
    try:
        if not ruta.exists():
            return default
        txt = ruta.read_text(encoding="utf-8").strip()
        if not txt:
            return default
        return json.loads(txt)
    except (json.JSONDecodeError, OSError):
        return default

# ---------------------------
# Búsquedas
# ---------------------------
def buscarAlumnoPorLegajo(legajo: int):
    """
    Retorna el dict del alumno o None.
    """
    alumnos = _leer_json(ALUMNOS_JSON, default=[])
    return next((a for a in alumnos if a.get("legajo") == legajo), None)

def buscarAlumnoPorLegajoNombreYApellido(legajo: int) -> str:
    """
    Retorna 'Nombre Apellido' o mensaje si no existe.
    """
    a = buscarAlumnoPorLegajo(legajo)
    if a:
        nombre = a.get("nombre", "").strip()
        apellido = a.get("apellido", "").strip()
        return f"{nombre} {apellido}".strip() or f"Alumno #{legajo}"
    return f"Alumno con legajo {legajo} no encontrado"

def buscarProfesorPorLegajo(legajo_profesor: int) -> str:
    """
    Retorna 'Nombre Apellido' del profesor o mensaje si no existe.
    """
    profesores = _leer_json(PROFESORES_JSON, default=[])
    p = next((x for x in profesores if x.get("legajo") == legajo_profesor), None)
    if p:
        return f"{p.get('nombre','').strip()} {p.get('apellido','').strip()}".strip()
    return f"Profesor con legajo {legajo_profesor} no encontrado"

def buscarCursoPorId(idCurso):
    """
    Retorna el dict del curso o None. Acepta 'AED1'/'aed1' o similar.
    """
    cursos = _leer_json(CURSOS_JSON, default=[])
    id_norm = str(idCurso).strip().upper()
    return next((c for c in cursos if str(c.get("id")).strip().upper() == id_norm), None)

def validarAlumnoYCurso(legajo, idCurso):
    """
    Retorna (alumno, curso) o (None, None) con mensaje si algo no existe.
    """
    alumno = buscarAlumnoPorLegajo(legajo)
    curso  = buscarCursoPorId(idCurso)
    if not alumno or not curso:
        print(headers.Fore.RED + "Alumno o curso inexistente.")
        return None, None
    return alumno, curso

# ---------------------------
# Pagos (búsqueda básica)
# ---------------------------
def buscarPagosPendientesPorLegajo(legajo: int):
    """
    Retorna lista de cuotas pendientes del alumno (cada item: dict con 'cuota_nro', 'legajo').
    """
    cuotas = _leer_json(CUOTAS_PEND_JSON, default=[])
    return [c for c in cuotas if c.get("legajo") == legajo]

# ---------------------------
# Placeholders (si alguien los llama)
# ---------------------------
def buscar_materia():
    # Si más adelante necesitás 'materia' distinta de 'curso', redefinir aquí.
    print("En desarrollo...")
    return None

def buscar_pagos():
    print("En desarrollo...")
    return None
