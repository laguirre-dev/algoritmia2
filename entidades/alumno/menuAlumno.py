import entidades.datos as datos
import utils.pantalla as headers
import gestion_accion
import gestion_visualizar

def menuOpciones():
    print("\n")
    headers.header("MENÚ ALUMNO")
    print(headers.Fore.GREEN + "1. Inscribirse en un curso")
    print(headers.Fore.GREEN + "2. Ver cursos disponibles")
    print(headers.Fore.GREEN + "3. Consultar pagos adeudados")
    print(headers.Fore.GREEN + "4. Ver estado de aprobación")
    print(headers.Fore.GREEN + "5. Ver mis cursos")
    print(headers.Fore.RED   + "6. Volver al menú principal")
    
def menuAlumno(legajo):
    """Muestra y gestiona el menú de opciones para un Alumno."""
    menuOpciones()
    opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
    while opcion != 6:
        if opcion == 1:

            gestion_visualizar.verCursosDisponibles(legajo)
            idCurso = input(headers.Fore.WHITE + "Ingrese el ID del curso al que desea inscribirse: ")
            gestion_accion.inscribirEnCurso(legajo, idCurso)

        elif opcion == 2:
            gestion_visualizar.verCursosDisponibles()
        elif opcion == 3:
            print(headers.Fore.GREEN + "Consultar pagos adeudados - Funcionalidad en desarrollo.")
        elif opcion == 4:
            gestion_visualizar.verEstadoAprobacion(legajo)
        elif opcion == 5:
            gestion_visualizar.verMisCursos(legajo)
        else:
            print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")
        menuOpciones()
        opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
    print(headers.Fore.RED + "Volviendo al menú principal...")
    
if __name__ == "__main__":
    menuAlumno()