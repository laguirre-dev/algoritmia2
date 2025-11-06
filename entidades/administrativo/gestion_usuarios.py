"""
El objetivo del modulo es centralizar las funcionalidades de usuarios para los administrativos

El administrativo debe poder:
Dar de alta y baja alumnos y profesores, asi como también cambiar la contraseña de ingreso

Consideraciones:
Al generar cualquier alta o baja, añade o elimina el legajo en la base CREDENCIALES
"""

import colorama
from entidades.datos import CREDENCIALES, ALUMNOS_DB, PROFESORES_DB
from utils.pantalla import limpiar_pantalla
from utils.credenciales import crear_clave, imprimir_credenciales


def alta_alumno():
    """
    La funcion realiza un append a la lista de alumnos y un append a la lista de credenciales con los datos solicitados
    """
    finaliza_alta = False
    cantidad = 0
    while not finaliza_alta:
        limpiar_pantalla()
        print("Ha seleccionado la opcion de dar de alta un alumno...\n")
        legajo = len(ALUMNOS_DB) + 1
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        clave = crear_clave(legajo, nombre, apellido)
        ALUMNOS_DB.append(
            {
                "legajo": legajo,
                "nombre": nombre,
                "apellido": apellido,
                "activo": True,
                "pagos_pendientes": [],
                "materias": [],
            }
        )
        CREDENCIALES.append({"legajo": legajo, "clave": clave, "rol": "alumno"})
        cantidad += 1
        print("Alumno dado de alta con exito.")
        imprimir_credenciales(legajo, clave)
        print(ALUMNOS_DB)
        opcion = input("\n¿Desea ingresar otro alumno? (s/n): ").strip().lower()
        if opcion != "s":
            finaliza_alta = True
            print("\nProceso de alta finalizado.")
            print("\nAlumnos creados: ", cantidad)
            input("Presione cualquier tecla...")
            limpiar_pantalla()
        else:
            limpiar_pantalla()


def baja_alumno():
    """
    La funcion realiza un filtrado de los legajos a medida que va solicitando al usuario final, luego pide confirmar legajo y realiza la baja del alumno
    Tiene en cuenta si el alumno ya está de baja
    """
    finaliza_baja = False
    cantidad = 0
    while not finaliza_baja:
        limpiar_pantalla()
        legajo_ingresado = input("Ingrese el legajo del alumno a dar de baja: ").strip()
        coincidencias_activas = list(
            filter(
                lambda alumno: legajo_ingresado in str(alumno["legajo"])
                and alumno["activo"],
                ALUMNOS_DB,
            )
        )
        if coincidencias_activas:
            print("Coincidencias encontradas (solo alumnos activos)")
            for alumno in coincidencias_activas:
                print(
                    f"Legajo: {alumno['legajo']}, Nombre: {alumno['nombre']}, Apellido: {alumno['apellido']}"
                )
            legajo_confirmado = input(
                "Ingrese el legajo exacto para confirmar o presione ENTER para cancelar: "
            ).strip()
            coincidencia_exacta = False
            for alumno in ALUMNOS_DB:
                if str(alumno["legajo"]) == legajo_confirmado:
                    alumno["activo"] = False
                    coincidencia_exacta = True
            if coincidencia_exacta:
                print("Alumno dado de baja con exito.")
                cantidad += 1
            else:
                print("Legajo ingresado no coincide con ninguna coincidencia.")
            print(ALUMNOS_DB)
            opcion = input("\n¿Desea dar de baja otro alumno? (s/n): ").strip().lower()
            if opcion != "s":
                finaliza_baja = True
                print("\nProceso de baja finalizado.")
                print("\nAlumnos dados de baja: ", cantidad)
                input("Presione cualquier tecla...")
                limpiar_pantalla()
            else:
                limpiar_pantalla()
        else:
            print("No se encontraron alumnos activos con el legajo: ", legajo_ingresado)
            opcion = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()
            if opcion != "s":
                finaliza_baja = True
                print("\nProceso de baja finalizado.")
                print("\nAlumnos dados de baja: ", cantidad)
                input("Presione cualquier tecla...")
                limpiar_pantalla()
            else:
                limpiar_pantalla()


############
# PROFESOR #
############
def alta_profesor():
    print("En desarrollo...")
    return


def baja_profesor():
    print("En desarrollo...")
    return


def mostrar_opciones():
    limpiar_pantalla()
    print("--- MENU ADMINISTRATIVO | GESTION DE USUARIOS ---")
    print("1. Dar de alta alumno")
    print("2. Dar de baja alumno")
    print("3. Dar de alta profesor")
    print("4. Dar de baja profesor")
    print("5. Ver usuarios activos")
    print("6. Ver usuarios inactivos")
    print("0. Salir")


def menu():
    mostrar_opciones()
    opcion = int(input("Seleccione una opcion: "))
    while opcion != 0:
        if opcion == 1:
            alta_alumno()
        elif opcion == 2:
            baja_alumno()
        elif opcion == 3:
            alta_profesor()
        elif opcion == 4:
            baja_profesor()
        elif opcion == 5:
            print("En desarrollo...")
        elif opcion == 6:
            print("En desarrollo...")
        else:
            print("Opcion no valida. Intente de nuevo.")
        mostrar_opciones()
        opcion = int(input("Seleccione una opcion: "))


menu()
