import json
from pathlib import Path
from utils import pantalla as headers
from utils import busquedas as busqueda

DATOS_DIR = Path(__file__).resolve().parents[1] / "datos"
CUOTAS_JSON = DATOS_DIR / "cuotas_pendientes.json"
ALUMNOS_JSON = DATOS_DIR / "alumnos.json"


# ---------------------------
# Funciones auxiliares
# ---------------------------
def _leer_lista_json(ruta: Path):
    """Lee una lista desde un archivo JSON. Si falla, devuelve lista vacía."""
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
    """Guarda una lista en formato JSON."""
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(headers.Fore.RED + "[ERROR IO] " + str(e))
        return False


# ---------------------------
# Funciones principales
# ---------------------------
def consultarPagos(legajo):
    """
    Muestra las cuotas pendientes del alumno según cuotas_pendientes.json.
    """
    alumno = busqueda.buscarAlumnoPorLegajo(legajo)
    if alumno is None:
        print(headers.Fore.RED + "Alumno inexistente.")
        return False

    cuotas = _leer_lista_json(CUOTAS_JSON)
    pendientes = [c for c in cuotas if "legajo" in c and c["legajo"] == legajo]

    headers.header("CUOTAS PENDIENTES")
    if len(pendientes) == 0:
        print(headers.Fore.GREEN + "No tenés cuotas pendientes. ¡Estás al día!")
        return True

    for cuota in pendientes:
        numero = cuota["cuota_nro"] if "cuota_nro" in cuota else "?"
        print(headers.Fore.WHITE + f"Cuota N° {numero} - Estado: Pendiente")

    return True


def pagarCuota(legajo):
    """
    Permite al alumno pagar una cuota pendiente (elimina del JSON).
    """
    alumno = busqueda.buscarAlumnoPorLegajo(legajo)
    if alumno is None:
        print(headers.Fore.RED + "Alumno inexistente.")
        return False

    cuotas = _leer_lista_json(CUOTAS_JSON)
    pendientes = [c for c in cuotas if "legajo" in c and c["legajo"] == legajo]

    if len(pendientes) == 0:
        print(headers.Fore.GREEN + "No tenés cuotas pendientes. ¡Todo en orden!")
        return True

    headers.header("PAGO DE CUOTAS")
    print(headers.Fore.WHITE + "Cuotas pendientes:")
    for cuota in pendientes:
        print(f"- Cuota N° {cuota['cuota_nro']}")

    try:
        numero = int(input(headers.Fore.WHITE + "Ingrese el número de cuota que desea pagar: "))
    except ValueError:
        print(headers.Fore.RED + "Debe ingresar un número de cuota válido.")
        return False

    # Verifico si existe esa cuota
    existe = False
    nuevas_cuotas = []
    for c in cuotas:
        if "legajo" in c and c["legajo"] == legajo and c["cuota_nro"] == numero:
            existe = True  # la omitimos (pagada)
        else:
            nuevas_cuotas.append(c)

    if not existe:
        print(headers.Fore.RED + "No se encontró una cuota pendiente con ese número.")
        return False

    # Guardamos la lista actualizada
    if _escribir_lista_json(CUOTAS_JSON, nuevas_cuotas):
        print(headers.Fore.GREEN + f"Pago de la cuota N° {numero} registrado correctamente.")
        return True
    else:
        print(headers.Fore.RED + "Error al registrar el pago.")
        return False
