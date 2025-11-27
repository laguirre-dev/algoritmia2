import os
from colorama import init, Fore, Style
from tabulate import tabulate
from utils import validaciones

init(autoreset=True)

def limpiarTerminal():
    os.system("cls" if os.name == "nt" else "clear")

def header(titulo):
    print(Fore.GREEN + "=" * 50)
    print(Style.BRIGHT + Fore.WHITE + titulo.center(50))
    print(Fore.GREEN + "=" * 50)

def green_text(texto): return print(Fore.GREEN + texto)
def red_text(texto): return print(Fore.RED + texto)
def yellow_text(texto): return print(Fore.YELLOW + texto)
def bold_text(texto): return Style.BRIGHT + texto

def imprime_datos(datos):
    limpiarTerminal()
    if not datos:
        print("No hay datos para mostrar.")
        return
    print(tabulate(datos, headers="keys", tablefmt="rounded_grid"))

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

def opcionesAlumnoPrincipal(): pass
def opcionesProfesorPrincipal(): pass

menu_segun_rol = {
    "principal": opcionesPrincipal,
    "alumno": opcionesAlumnoPrincipal,
    "profesor": opcionesProfesorPrincipal,
    "administrativo": opcionesAdministrativoPrincipal
}

def mostrarMenu(tipo, opciones):
    limpiarTerminal()
    if tipo in menu_segun_rol:
        menu_segun_rol[tipo]()
    else:
        print("Menú no definido")
    
    opcion = validaciones.validaOpcion(opciones_permitidas=opciones)
    return opcion