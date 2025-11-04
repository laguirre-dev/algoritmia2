import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ALUMNOS_JSON = BASE_DIR / "alumnos.json"
PROFESORES_JSON = BASE_DIR / "profesores.json"
CURSOS_JSON = BASE_DIR / "cursos.json"
CUOTAS_JSON = BASE_DIR / "cuotas_pendientes.json"
CREDENCIALES_JSON = BASE_DIR / "credenciales.json"

def _leer_json(ruta):
    try:
        with ruta.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

ALUMNOS_DB = _leer_json(ALUMNOS_JSON)
PROFESORES_DB = _leer_json(PROFESORES_JSON)
CURSOS_DB = _leer_json(CURSOS_JSON)
CUOTAS_PENDIENTES = _leer_json(CUOTAS_JSON)
CREDENCIALES = _leer_json(CREDENCIALES_JSON)
