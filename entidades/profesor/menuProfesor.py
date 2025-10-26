from entidades import datos as datos
from utils import pantalla as headers
from utils import busquedas as buscar
from . import gestion_visualizar
from . import gestion_evaluar
from . import gestion_reportes

def menuOpciones(legajoProfesor):
    
    print(headers.Fore.GREEN + f"¡Bienvenido Profesor {buscar.buscarProfesorPorLegajo(legajoProfesor)} !\n")
    
    print(headers.Fore.GREEN + "1. Visualizar cursos y aulas")
    print(headers.Fore.GREEN + "2. Aprobar o desaprobar alumnos")
    print(headers.Fore.GREEN + "3. Generar reporte de alumnos")
    print(headers.Fore.GREEN + "4. Mis gestiones -- En desarrollo")
    print(headers.Fore.RED   + "5. Volver al menú principal")

def menuVisualizar():
    headers.header("MENÚ PROFESOR - ALUMNOS Y CURSOS")
    print(headers.Fore.GREEN + "1. Mis cursos")
    print(headers.Fore.GREEN + "2. Mis alumnos")
    print(headers.Fore.GREEN + "3. Alumno Conocido")
    print(headers.Fore.RED   + "4. Volver al menú profesor")
    
def menuGenerarReportes():
    headers.header("MENÚ PROFESOR - REPORTES")
    print(headers.Fore.GREEN + "1. Mis alumnos")
    print(headers.Fore.GREEN + "2. Mis alumnos aprobados")
    print(headers.Fore.GREEN + "3. Mis cursos")
    print(headers.Fore.RED   + "4. Volver al menú profesor")
    
def menuGestiones():
    headers.header("MENÚ PROFESOR - GESTIONES")
    print(headers.Fore.GREEN + "1. Pedir Baja")
    print(headers.Fore.GREEN + "2. Dia de Examen")
    print(headers.Fore.RED   + "3. Volver al menú profesor")

def menuProfesor(legajoProfesor):
    menuOpciones(legajoProfesor)
    opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
    while opcion != 5:
        if opcion == 1:
            menuVisualizar()
            subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            while subopcion != 4:
                if subopcion == 1:
                    gestion_visualizar.verMisCursos(legajoProfesor)
                elif subopcion == 2:
                    gestion_visualizar.verMisAlumnos(legajoProfesor)
                elif subopcion == 3:
                    gestion_visualizar.alumnoConocido(legajoProfesor)
                else:
                    print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")
                menuVisualizar()
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))

        elif opcion == 2:
            gestion_evaluar.aprobarODesaprobarAlumnos(legajoProfesor)

        elif opcion == 3:
            menuGenerarReportes()
            subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            while subopcion != 4:
                if subopcion == 1:  
                    try:  
                        gestion_reportes.generarReporteDeAlumno(legajoProfesor)
                        print(headers.Fore.GREEN + "Se generó el reporte de Alumnos!")
                    except FileNotFoundError:
                        print(headers.Fore.RED + "No se pudo generar el reporte pedido.")
                elif subopcion == 2:
                    try:  
                        gestion_reportes.generarReporteDeAlumnosAprobados(legajoProfesor)
                        print(headers.Fore.GREEN + "Se generó el reporte de Alumnos Aprobados!")
                    except FileNotFoundError:
                        print(headers.Fore.RED + "No se pudo generar el reporte pedido.")
                elif subopcion == 3:
                    try:  
                        gestion_reportes.generarReporteDeCursos(legajoProfesor)
                        print(headers.Fore.GREEN + "Se generó el reporte de tus Cursos!")
                    except FileNotFoundError:
                        print(headers.Fore.RED + "No se pudo generar el reporte pedido.")
                else:
                    print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")
                menuGenerarReportes()  
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))

        elif opcion == 4:
            menuGestiones()
            subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            while subopcion != 3:
                if subopcion == 1:
                    pass
                elif subopcion == 2:
                    pass
                else:
                    print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")
                menuGestiones()
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))

        else:
            print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")

        menuOpciones(legajoProfesor)
        opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))

    print(headers.Fore.RED + "Volviendo al menú principal...")

    