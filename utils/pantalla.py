import os
from colorama import init, Fore, Style
from tabulate import tabulate
import entidades.datos as datos

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


def muestraCredenciales():
    imprimeDatos(datos.CREDENCIALES)


def opcionesPrincipal():
    print("")
    header("| SISTEMA DE GESTIÓN DE ALUMNOS |")
    greenText("1. Iniciar sesión")
    redText("2. Salir del programa")
    print("")


# -- Administrativo: Principal -- #
def opcionesAdministrativoPrincipal():
    header("| MENÚ ADMINISTRATIVO |")
    greenText("1. Gestion de Usuarios")
    greenText("2. Gestion de Cursos")
    greenText("3. Gestion de Pagos")
    redText("4. Volver al menú principal")
    return


# -- Administrativo: Gestion de Usuarios -- #
def opcionesAdministrativoUsuarios():
    header("| GESTION DE USUARIOS |")
    greenText("1. Agregar Alumno")
    greenText("2. Agregar Profesor")
    greenText("3. Restableecer credenciales")  # se le pasa legajo
    redText("4. Volver al menú anterior")


# -- Administrativo: Gestion de Cursos -- #
def opcionesAdministrativoCursos():
    header("| GESTION DE CURSOS |")
    greenText("1. Agregar Curso")  # no se puede repetir idCurso
    greenText("2. Eliminar Curso")  # se le pasa id
    greenText("3. Asignar Profesor a Curso")  # se le pasa legajo
    greenText("4. Generar reporte de Cursos")  # apunta a la lista CURSOS
    redText("5. Volver al menú anterior")


# -- Administrativo: Gestion de Pagos -- #
def opcionesAdministrativoPagos():
    header("| GESTION DE PAGOS |")
    greenText("1. Sumar Pago Pendiente")  # legajo, cuota
    greenText("2. Generar reporte de Deudores")  # apunta a la lista CUOTAS_PENDIENTES
    redText("3. Volver al menú anterior")


def opcionesAlumnoPrincipal():
    return


def opcionesProfesorPrincipal():
    return
