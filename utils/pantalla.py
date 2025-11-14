import os
from colorama import init, Fore, Style
from tabulate import tabulate
from utils import validaciones

init(autoreset=True)


def limpiarTerminal():
    """
    Funcion para limpiar los mensajes de la consola
    """
    os.system("cls" if os.name == "nt" else "clear")


def header(titulo):
    """
    Imprime titulo en consola rodeado de hashtags verdes
    """
    print(Fore.GREEN + "=" * 50)
    print(Style.BRIGHT + Fore.WHITE + titulo.center(50))
    print(Fore.GREEN + "=" * 50)
    return


def greenText(texto):
    """
    Imprime mensaje de color verde en consola
    """
    return print(Fore.GREEN + texto)


def redText(texto):
    """
    Imprime mensaje de color rojo en consola
    """
    return print(Fore.RED + texto)


def yellowText(texto):
    """
    Imprime mensaje de color amarillo
    """
    return print(Fore.YELLOW + texto)


def boldText(texto):
    """
    Imprime mensaje con negrita aplicada en consola
    """
    return Style.BRIGHT + texto


def imprimeDatos(datos):
    limpiarTerminal()
    print(tabulate(datos, headers="keys", tablefmt="rounded_grid"))
    return


def opcionesPrincipal():
    print("")
    header("| SISTEMA DE GESTIÓN DE ALUMNOS |")
    greenText("1. Iniciar sesión")
    redText("2. Salir del programa")
    print("")


########### ADMINISTRATIVO


def opcionesAdministrativoPrincipal():
    header("| MENÚ ADMINISTRATIVO |")
    greenText("1. Ver todas las credenciales de los usuarios")
    greenText("2. Gestion de Usuarios")
    greenText("3. Gestion de Cursos")
    greenText("4. Gestion de Pagos")
    redText("0. Volver al menú principal")
    return


def opcionesAdministrativoUsuarios():
    header("| GESTION DE USUARIOS |")
    greenText("1. Agregar Alumno")
    greenText("2. Agregar Profesor")
    greenText("3. Restableecer credenciales")  # se le pasa legajo
    redText("4. Volver al menú principal")


def opcionesAdministrativoCursos():
    header("| GESTION DE CURSOS |")
    greenText("1. Agregar Curso") # no se puede repetir idCurso
    greenText("2. Eliminar Curso") # se le pasa id
    greenText("3. Generar reporte de Cursos") # apunta a la lista CURSOS
    redText("4. Volver al menú principal")


def opcionesAdministrativoPagos():
    header("| GESTION DE PAGOS |")
    greenText("1. Sumar Pago Pendiente") # legajo, cuota 
    greenText("2. Generar reporte de Deudores") # apunta a la lista CUOTAS_PENDIENTES
    redText("3. Volver al menú principal")


########### ADMINISTRATIVO


def opcionesAlumnoPrincipal():
    return


def opcionesProfesorPrincipal():
    return


menuSegunRol = {
    "principal": opcionesPrincipal,
    "alumno": opcionesAlumnoPrincipal,
    "profesor": opcionesProfesorPrincipal,
    "administrativo": opcionesAdministrativoPrincipal,
    "admin_usuarios": opcionesAdministrativoUsuarios,
    "admin_cursos": opcionesAdministrativoCursos,
    "admin_pagos": opcionesAdministrativoPagos,
}


def mostrarMenu(tipo, opciones):
    limpiarTerminal()
    menuSegunRol[tipo]()
    opcion = validaciones.validaOpcion(opciones)
    return opcion
