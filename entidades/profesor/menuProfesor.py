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
    try:
        opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
    except ValueError:
        opcion = 0

    while opcion != 5:
        if opcion == 1:
            menuVisualizar()
            
            try:
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            except ValueError:
                subopcion = 0
                
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
                
                try:
                    subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
                except ValueError:
                    subopcion = 0

        elif opcion == 2:
            try:
                gestion_evaluar.aprobarODesaprobarAlumnos(legajoProfesor)
            except Exception as e:
                print(headers.Fore.RED + f"Error al evaluar alumnos: {e}")

        elif opcion == 3:
            menuGenerarReportes()
            
            try:
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            except ValueError:
                subopcion = 0
                
            while subopcion != 4:
                if subopcion == 1:  
                    try:  
                        gestion_reportes.generarReporteDeAlumno(legajoProfesor)
                        print(headers.Fore.GREEN + "Se generó el reporte de Alumnos!")
                    except Exception as e:
                        print(headers.Fore.RED + f"No se pudo generar el reporte: {e}")
                elif subopcion == 2:
                    try:  
                        gestion_reportes.generarReporteDeAlumnosAprobados(legajoProfesor)
                        print(headers.Fore.GREEN + "Se generó el reporte de Alumnos Aprobados!")
                    except Exception as e:
                        print(headers.Fore.RED + f"No se pudo generar el reporte: {e}")
                elif subopcion == 3:
                    try:  
                        gestion_reportes.generarReporteDeCursos(legajoProfesor)
                        print(headers.Fore.GREEN + "Se generó el reporte de tus Cursos!")
                    except Exception as e:
                        print(headers.Fore.RED + f"No se pudo generar el reporte: {e}")
                else:
                    print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")
                menuGenerarReportes() 
                 
                try:
                    subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
                except ValueError:
                    subopcion = 0

        elif opcion == 4:
            menuGestiones()
            try:
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            except ValueError:
                subopcion = 0
            while subopcion != 3:
                if subopcion == 1:
                    print(headers.Fore.YELLOW + "Funcionalidad 'Pedir Baja' en desarrollo...")
                elif subopcion == 2:
                    print(headers.Fore.YELLOW + "Funcionalidad 'Día de Examen' en desarrollo...")
                else:
                    print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")
                menuGestiones()
                try:
                    subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
                except ValueError:
                    subopcion = 0

        else:
            print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")

        menuOpciones(legajoProfesor)
        try:
            opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
        except ValueError:
            opcion = 0

    print(headers.Fore.RED + "Volviendo al menú principal...")


    