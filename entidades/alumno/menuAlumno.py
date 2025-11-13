import entidades.datos as datos
from utils import pantalla as headers
from utils import busquedas as buscar
from . import gestion_accion
from . import gestion_visualizar
from . import gestion_pagos
from . import gestion_reportes

def menuOpciones(legajoAlumno):
    
    print(headers.Fore.GREEN + f"¡Bienvenido Alumno {buscar.buscarAlumnoPorLegajoNombreYApellido(legajoAlumno)} !\n")
    
    print(headers.Fore.GREEN + "1. Gestiones alumno")
    print(headers.Fore.GREEN + "2. Visualizar información")
    print(headers.Fore.GREEN + "3. Pagos -- En desarrollo")
    print(headers.Fore.GREEN + "4. Generar reportes")
    print(headers.Fore.RED   + "5. Volver al menú principal")

def menuAcciones():
    headers.header("MENÚ ALUMNO - ACCIONES")
    print(headers.Fore.GREEN + "1. Inscribirse en un curso")
    print(headers.Fore.GREEN + "2. Darse de baja de un curso")
    print(headers.Fore.RED   + "3. Volver al menú alumno")

def menuVisualizar():
    headers.header("MENÚ ALUMNO - VISUALIZAR")
    print(headers.Fore.GREEN + "1. Ver mis cursos")
    print(headers.Fore.GREEN + "2. Ver estado de aprobación")
    print(headers.Fore.RED   + "3. Volver al menú alumno")

def menuPagos():
    headers.header("MENÚ ALUMNO - PAGOS")
    print(headers.Fore.GREEN + "1. Consultar pagos adeudados")
    print(headers.Fore.GREEN + "2. Pagar cuotas adeudadas")
    print(headers.Fore.RED   + "3. Volver al menú alumno")

def menuGenerarReportes():
    headers.header("MENÚ ALUMNO - REPORTES")
    print(headers.Fore.GREEN + "1. Generar reporte de mis cursos inscriptos")
    print(headers.Fore.RED   + "2. Volver al menú alumno")

def menuAlumno(legajoAlumno):
    menuOpciones(legajoAlumno)
    try:
        opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
    except ValueError:
        opcion = 0

    while opcion != 5:
        if opcion == 1:
            menuAcciones()
            
            try:
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            except ValueError:
                subopcion = 0
                
            while subopcion != 3:
                
                if subopcion == 1:
                    gestion_visualizar.verCursosDisponibles(legajoAlumno)
                    idCurso = input(headers.Fore.WHITE + "Ingrese el ID del curso al que desea inscribirse: ")
                    gestion_accion.inscribirEnCurso(legajoAlumno, idCurso)
                elif subopcion == 2:
                    gestion_visualizar.verMisCursos(legajoAlumno)
                    idCurso = input(headers.Fore.WHITE + "Ingrese el ID del curso del que desea darse de baja: ")
                    gestion_accion.darseDeBaja(legajoAlumno, idCurso)
                else:
                    print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")
                menuAcciones()
                
                try:
                    subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
                except ValueError:
                    subopcion = 0

        elif opcion == 2:
            menuVisualizar()
            
            try:
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            except ValueError:
                subopcion = 0
                
            while subopcion != 3:
                if subopcion == 1:
                    gestion_visualizar.verMisCursos(legajoAlumno)
                elif subopcion == 2:
                    gestion_visualizar.verEstadoAprobacion(legajoAlumno)
                else:
                    print(headers.Fore.RED + "Opción no válida.")
                menuVisualizar()
                
                try:
                    subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
                except ValueError:
                    subopcion = 0

        elif opcion == 3:
            menuPagos()
            
            try:
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            except ValueError:
                subopcion = 0
                
            while subopcion != 3:
                if subopcion == 1:
                    gestion_pagos.consultarPagos(legajoAlumno)
                elif subopcion == 2:
                    gestion_pagos.pagarCuota(legajoAlumno)
                else:
                    print(headers.Fore.RED + "Opción no válida.")
                menuPagos()
                
                try:
                    subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
                except ValueError:
                    subopcion = 0

        elif opcion == 4:
            menuGenerarReportes()
            
            try:
                subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
            except ValueError:
                subopcion = 0
                
            while subopcion != 2:
                if subopcion == 1:
                    
                    try:
                        gestion_reportes.generarReporteDeCursosAlumno(legajoAlumno)
                    except Exception as e:
                        print(headers.Fore.RED + f"Error al generar reporte: {e}")
                
                else:
                    print(headers.Fore.RED + "Opción no válida.")
                menuGenerarReportes()
                
                try:
                    subopcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
                except ValueError:
                    subopcion = 0

        else:
            print(headers.Fore.RED + "Opción no válida.")

        menuOpciones(legajoAlumno)
        try:
            opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
        except ValueError:
            opcion = 0

    print(headers.Fore.RED + "Volviendo al menú principal...")