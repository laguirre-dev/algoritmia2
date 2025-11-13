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


def green_text(texto):
    """
    Imprime mensaje de color verde en consola
    """
    return print(Fore.GREEN + texto)


def red_text(texto):
    """
    Imprime mensaje de color rojo en consola
    """
    return print(Fore.RED + texto)


def yellow_text(texto):
    """
    Imprime mensaje de color amarillo
    """
    return print(Fore.YELLOW + texto)


def bold_text(texto):
    """
    Imprime mensaje con negrita aplicada en consola
    """
    return Style.BRIGHT + texto


def imprime_datos(datos):
    limpiarTerminal()
    print(tabulate(datos, headers="keys", tablefmt="rounded_grid"))
    return


def opcionesPrincipal():
    print("")
    header("| SISTEMA DE GESTIÓN DE ALUMNOS |")
    green_text("1. Iniciar sesión")
    red_text("2. Salir del programa")
    print("")


def opcionesAdministrativoPrincipal():
    header("| MENÚ ADMINISTRATIVO |")
    green_text("1. Ver todas las credenciales de los usuarios") # y generar archivo
    green_text("2. Gestion de Usuarios") # genera profesor o alumno y restablecer credenciales 
    green_text("3. Gestion de Cursos") # alta/baja cursos
    green_text("4. Gestion de Pagos") # Agrega cuotas con la condicion de que no se pueda agregar la misma cuota si ya esta creada. Generar reporte de Deudores. 
    red_text("0. Volver al menú principal")
    return

def opcionesAlumnoPrincipal(): return

def opcionesProfesorPrincipal(): return


menu_segun_rol = {
    "principal": opcionesPrincipal,
    "alumno": opcionesAlumnoPrincipal,
    "profesor": opcionesProfesorPrincipal,
    "administrativo": opcionesAdministrativoPrincipal
}

def mostrar_menu(tipo, opciones):
    limpiarTerminal()
    menu_segun_rol[tipo]()
    opcion = validaciones.valida_opcion(opciones)
    return opcion
