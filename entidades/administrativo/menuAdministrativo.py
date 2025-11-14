import entidades.datos as datos
from utils import pantalla
from . import gestion_cursos, gestion_pagos, gestion_usuarios
from colorama import Fore

def muestraCredenciales():
    pantalla.imprimeDatos(datos.CREDENCIALES)


logica_seleccion_menu = {
    1: muestraCredenciales,
    2: gestion_usuarios.menuGestionUsuarios,
    3: gestion_cursos.menu_gestion_curso,
    4: gestion_pagos.menu_gestion_pagos,
}


def asignarCursoAProfesor(legajoProf):
    profesorEncontrado = next(
        (p for p in datos.PROFESORES_DB if p["legajo"] == legajoProf), None
    )
    if not profesorEncontrado:
        print(Fore.RED + "Profesor no encontrado.")
        return
    if datos.CURSOS_DB:
        pantalla.header("CURSOS DISPONIBLES")
        for curso in datos.CURSOS_DB:
            prof = next(
                (p for p in datos.PROFESORES_DB if p["legajo"] == curso["profesor"]),
                None,
            )
            nombreProf = (
                f"{prof['nombre']} {prof['apellido']}" if prof else "Sin asignar"
            )
            pantalla.yellowText(
                f"{curso['id']} - {curso['nombre']} (Profesor: {nombreProf})"
            )
        idCurso = input(pantalla.boldText("Ingrese el ID del curso a asignar: "))
        cursoEncontrado = next((c for c in datos.CURSOS_DB if c["id"] == idCurso), None)
        if not cursoEncontrado:
            pantalla.redText("Curso no encontrado.")
            return
        cursoEncontrado["profesor"] = profesorEncontrado["legajo"]
        if cursoEncontrado["id"] not in profesorEncontrado["materias"]:
            profesorEncontrado["materias"].append(cursoEncontrado["id"])
        pantalla.greenText(
            f"Curso {cursoEncontrado['nombre']} asignado al profesor {profesorEncontrado['nombre']}."
        )
    else:
        pantalla.redText(
            "No hay cursos disponibles. Por favor ingresar un curso primero."
        )
        return


def aprobarPago():
    """
    Aprueba el pago de un alumno (mueve de pendientes a pagadas).
    """
    pantalla.header("APROBAR PAGO")
    legajo = int(input(Fore.WHITE + "Ingrese el legajo del alumno: "))
    cuotas = [c for c in datos.CUOTAS_PENDIENTES if c["legajo"] == legajo]

    if not cuotas:
        print(Fore.RED + "El alumno no tiene pagos pendientes.")
        return

    print(Fore.WHITE + "Pagos pendientes:")
    for cuota in cuotas:
        print(Fore.WHITE + f"Cuota N°{cuota['cuota_nro']}")

    nro = int(input(Fore.WHITE + "Ingrese el número de cuota a aprobar: "))
    cuota = next((c for c in cuotas if c["cuota_nro"] == nro), None)

    if cuota:
        datos.CUOTAS_PENDIENTES.remove(cuota)
        print(Fore.GREEN + f"Pago de cuota N°{nro} aprobado para el alumno {legajo}.")
    else:
        print(Fore.RED + "Número de cuota inválido.")


def menuAdministrativo(legajo):
    """Muestra el menú de opciones para un Administrativo."""
    pantalla.greenText(f"Hola administrativo: {legajo}")
    pantalla.opcionesAdministrativoPrincipal()
    opcion = int(input("Elija una opcion del menu para continuar: "))
    try:
        while opcion != 0:
            logica_seleccion_menu[opcion]()
            pantalla.opcionesAdministrativoPrincipal()
            opcion = int(input("Elija una opcion del menu para continuar: "))
    except Exception as e:
        print(e)
    return


if __name__ == "__main__":
    menuAdministrativo()
