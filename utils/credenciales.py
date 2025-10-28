import json
from pathlib import Path
import utils.pantalla as headers

# Carpeta de datos: .../entidades/datos (desde utils/)
DATOS_DIR = Path(__file__).resolve().parents[1] / "entidades" / "datos"
CREDENCIALES_JSON = DATOS_DIR / "credenciales.json"


def _leer_lista_json(ruta: Path):
    """
    Lee una lista desde un archivo JSON.
    Si el archivo no existe o hay error, devuelve [].
    """
    try:
        with ruta.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except Exception:
        return []


def crear_clave(legajo, nombre, apellido):
    """
    Crea una clave con el formato: legajo + primera letra nombre (mayúscula) + apellido en minúsculas.
    Ejemplo: 105 + F + kerekes -> 105Fkerekes
    """
    parte1 = str(legajo)
    parte2 = nombre[0].upper() if nombre != "" else ""
    parte3 = apellido.lower()
    return parte1 + parte2 + parte3


def login(legajo, clave):
    """
    Verifica si las credenciales coinciden con las guardadas en credenciales.json.
    Devuelve (True, rol) si son correctas, o (False, False) si no.
    """
    credenciales = _leer_lista_json(CREDENCIALES_JSON)

    for credencial in credenciales:
        if "legajo" in credencial and "clave" in credencial and "rol" in credencial:
            if credencial["legajo"] == legajo and credencial["clave"] == clave:
                return True, credencial["rol"]

    print(headers.Fore.RED + "Credenciales incorrectas. Inténtelo nuevamente.")
    return False, False


def imprimir_credenciales(legajo, clave):
    """
    Muestra las credenciales generadas por pantalla.
    """
    print("\n#####################")
    print("Legajo:", legajo)
    print("Clave:", clave)
    print("#####################\n")
