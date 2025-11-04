"""
El objetivo del modulo es centralizar las funcionalidades de usuarios para los administrativos

Altas, bajas de alumnos y profesores
lenguaje tecnico:
crea un diccionario Alumno y lo añade a la lista

Consideraciones:
Al generar cualquier alta o baja, añade o elimina el legajo en la base CREDENCIALES
"""

import json
from pathlib import Path
from utils.pantalla import limpiarTerminal
from utils.credenciales import crear_clave as crearClave, imprimir_credenciales as imprimirCredenciales

# rutas a los archivos JSON
BASE_DIR = Path(__file__).resolve().parents[3] / "baseDeDatos"
ALUMNOS_JSON = BASE_DIR / "alumnos.json"
CREDENCIALES_JSON = BASE_DIR / "credenciales.json"

def leerLista(ruta: Path):
    try:
        with ruta.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except:
        return []

def escribirLista(ruta: Path, data):
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False


def altaAlumno():
    """
    La funcion realiza un append a la lista de alumnos y un append a la lista de credenciales con los datos solicitados
    """
    finalizaAlta = False
    cantidad = 0
    while not finalizaAlta:
        limpiarTerminal()
        print("Ha seleccionado la opcion de dar de alta un alumno...\n")

        alumnos = leerLista(ALUMNOS_JSON)
        credenciales = leerLista(CREDENCIALES_JSON)

        # calculo nuevo legajo
        maxLegajo = max([a.get("legajo", 0) for a in alumnos], default=100)
        legajo = maxLegajo + 1
        print(f"Legajo: {legajo}")

        nombre = input("Ingrese el nombre del alumno: ").strip()
        apellido = input("Ingrese el apellido del alumno: ").strip()

        clave = crearClave(legajo, nombre, apellido)

        # crea el diccionario alumno
        alumnos.append({
            "legajo": legajo,
            "nombre": nombre,
            "apellido": apellido,
            "activo": True,
            "pagos_pendientes": [],
            "materias": []
        })

        # agrega credencial asociada
        credenciales.append({
            "legajo": legajo,
            "clave": clave,
            "rol": "alumno"
        })

        ok1 = escribirLista(ALUMNOS_JSON, alumnos)
        ok2 = escribirLista(CREDENCIALES_JSON, credenciales)

        if ok1 and ok2:
            print("Alumno dado de alta con exito.")
            imprimirCredenciales(legajo, clave)
            cantidad += 1
        else:
            print("No se pudo guardar la información.")

        opcion = input("\n¿Desea ingresar otro alumno? (s/n): ").strip().lower()
        if opcion != "s":
            finalizaAlta = True
            print("\nProceso de alta finalizado.")
            print("\nAlumnos creados: ", cantidad)
            input("Presione cualquier tecla...")
            limpiarTerminal()
        else:
            limpiarTerminal()


def bajaAlumno():
    """
    La funcion realiza un filtrado de los legajos a medida que va solicitando al usuario final,
    luego pide confirmar legajo y realiza la baja del alumno.
    Tiene en cuenta si el alumno ya está de baja.
    """
    finalizaBaja = False
    cantidad = 0
    while not finalizaBaja:
        limpiarTerminal()
        legajoIngresado = input("Ingrese el legajo del alumno a dar de baja: ").strip()

        if not legajoIngresado.isdigit():
            print("Legajo inválido.")
            opcion = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()
            if opcion != "s":
                finalizaBaja = True
            continue

        legajo = int(legajoIngresado)

        alumnos = leerLista(ALUMNOS_JSON)
        credenciales = leerLista(CREDENCIALES_JSON)

        coincidenciasActivas = list(
            filter(
                lambda alumno: legajoIngresado in str(alumno["legajo"]) and alumno.get("activo", True),
                alumnos
            )
        )

        if coincidenciasActivas:
            print("Coincidencias encontradas (solo alumnos activos)")
            for alumno in coincidenciasActivas:
                print(f"Legajo: {alumno['legajo']}, Nombre: {alumno['nombre']}, Apellido: {alumno['apellido']}")

            legajoConfirmado = input("Ingrese el legajo exacto para confirmar o presione ENTER para cancelar: ").strip()
            coincidenciaExacta = False

            for alumno in alumnos:
                if str(alumno["legajo"]) == legajoConfirmado:
                    alumno["activo"] = False
                    coincidenciaExacta = True

            if coincidenciaExacta:
                credenciales = [c for c in credenciales if str(c.get("legajo")) != legajoConfirmado]
                ok1 = escribirLista(ALUMNOS_JSON, alumnos)
                ok2 = escribirLista(CREDENCIALES_JSON, credenciales)
                if ok1 and ok2:
                    print("Alumno dado de baja con exito.")
                    cantidad += 1
                else:
                    print("No se pudo guardar la baja.")
            else:
                print("Legajo ingresado no coincide con ninguna coincidencia.")

            opcion = input("\n¿Desea dar de baja otro alumno? (s/n): ").strip().lower()
            if opcion != "s":
                finalizaBaja = True
                print("\nProceso de baja finalizado.")
                print("\nAlumnos dados de baja: ", cantidad)
                input("Presione cualquier tecla...")
                limpiarTerminal()
            else:
                limpiarTerminal()
        else:
            print("No se encontraron alumnos activos con el legajo:", legajoIngresado)
            opcion = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()
            if opcion != "s":
                finalizaBaja = True
                print("\nProceso de baja finalizado.")
                print("\nAlumnos dados de baja: ", cantidad)
                input("Presione cualquier tecla...")
                limpiarTerminal()
            else:
                limpiarTerminal()


############
# PROFESOR #
############
def altaProfesor():
    print("En desarrollo...")
    return

def bajaProfesor():
    print("En desarrollo...")
    return


def mostrarOpciones():
    limpiarTerminal()
    print("--- MENU ADMINISTRATIVO | GESTION DE USUARIOS ---")
    print("1. Dar de alta alumno")
    print("2. Dar de baja alumno")
    print("3. Dar de alta profesor")
    print("4. Dar de baja profesor")
    print("5. Ver usuarios activos")
    print("6. Ver usuarios inactivos")
    print("0. Salir")


def menuUsuarios():
    mostrarOpciones()
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        opcion = -1

    while opcion != 0:
        if opcion == 1:
            altaAlumno()
        elif opcion == 2:
            bajaAlumno()
        elif opcion == 3:
            altaProfesor()
        elif opcion == 4:
            bajaProfesor()
        elif opcion == 5:
            print("En desarrollo...")
        elif opcion == 6:
            print("En desarrollo...")
        else:
            print("Opcion no valida. Intente de nuevo.")
        mostrarOpciones()
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            opcion = -1
