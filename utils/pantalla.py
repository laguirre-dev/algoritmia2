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
    greenText("1. Sumar Pago Pendiente") # legajo, cuota 
    greenText("2. Generar reporte de Deudores") # apunta a la lista CUOTAS_PENDIENTES
    redText("3. Volver al menú principal")


########### ALUMNO

def opcionesAlumnoPrincipal(legajoAlumno):
    """
    Menú principal del Alumno.
    """
    header("| MENÚ ALUMNO |")

    print(Fore.MAGENTA + f"¡Bienvenido Alumno {legajoAlumno} !\n") 
    
    print(greenText("1. Gestiones alumno"))
    print(greenText("2. Visualizar información"))
    print(greenText("3. Pagos"))
    print(greenText("4. Generar reportes"))
    print(redText("5. Volver al menú principal"))


def menuAccionesAlumno():
    """
    Submenú de Acciones del Alumno (Inscripción/Baja).
    """
    header("MENÚ ALUMNO - ACCIONES")
    print(greenText("1. Inscribirse en un curso"))
    print(greenText("2. Darse de baja de un curso"))
    print(redText("3. Volver al menú alumno"))


def menuVisualizarAlumno():
    """
    Submenú de Visualización del Alumno (Cursos/Aprobación).
    """
    header("| MENÚ ALUMNO - VISUALIZAR |")
    print(greenText("1. Ver mis cursos"))
    print(greenText("2. Ver estado de aprobación"))
    print(redText("3. Volver al menú alumno"))


def menuPagosAlumno():
    """
    Submenú de Pagos del Alumno (Consulta/Pago).
    """
    header("| MENÚ ALUMNO - PAGOS |")
    print(greenText("1. Consultar pagos adeudados"))
    print(greenText("2. Pagar cuotas adeudadas")) 
    print(redText("3. Volver al menú alumno"))


def menuGenerarReportesAlumno():
    """
    Submenú de Reportes del Alumno.
    """
    header("| MENÚ ALUMNO - REPORTES |")
    print(greenText("1. Generar reporte de mis cursos inscriptos"))
    print(redText("2. Volver al menú alumno"))


########### PROFESOR

def opcionesProfesorPrincipal(legajoProfesor):
    """
    Menú principal del Profesor.
    """
    header("| MENÚ PROFESOR |")

    print(Fore.MAGENTA + f"¡Bienvenido Profesor {legajoProfesor} !\n") 
    

    print(greenText("1. Visualizar cursos y aulas"))
    print(greenText("2. Aprobar o desaprobar alumnos"))
    print(greenText("3. Generar reporte de alumnos"))
    print(greenText("4. Mis gestiones"))
    print(redText("5. Volver al menú principal"))


def menuVisualizarProfesor():
    """
    Submenú de Visualización del Profesor (Alumnos y Cursos).
    """
    header("| MENÚ PROFESOR - ALUMNOS Y CURSOS |")
    print(greenText("1. Mis cursos"))
    print(greenText("2. Mis alumnos"))
    print(greenText("3. Alumno Conocido"))
    print(redText("4. Volver al menú profesor"))


def menuGenerarReportesProfesor():
    """
    Submenú de Reportes del Profesor.
    """
    header("| MENÚ PROFESOR - REPORTES |")
    print(greenText("1. Mis alumnos"))
    print(greenText("2. Mis alumnos aprobados"))
    print(greenText("3. Mis cursos"))
    print(redText("4. Volver al menú profesor"))


def menuGestionesProfesor():
    """
    Submenú de Gestiones del Profesor (Día de Examen).
    """
    header("| MENÚ PROFESOR - GESTIONES |")
    print(greenText("1. Dia de Examen"))
    print(redText("2. Volver al menú profesor"))