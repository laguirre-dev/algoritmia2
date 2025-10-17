from entidades import datos as datos
from utils import pantalla as headers
from utils import busquedas as buscar
from . import gestion_visualizar
from . import gestion_evaluar

def menuOpciones(legajoProfesor):
    # headers.header("MENÚ PROFESOR")
    
    print(headers.Fore.GREEN + f"¡Bienvenido Profesor {buscar.buscar_profesor(legajoProfesor)} !")
    print(headers.Fore.GREEN + "1. Visualizar cursos y aulas")
    print(headers.Fore.GREEN + "2. Aprobar o desaprobar alumnos")
    print(headers.Fore.GREEN + "3. Generar reporte de alumnos -- En desarrollo")
    print(headers.Fore.GREEN + "4. Mis gestiones -- En desarrollo")
    print(headers.Fore.RED   + "5. Volver al menú principal")

def menuVisualizar():
    headers.header("MENÚ PROFESOR - ALUMNOS Y CURSOS")
    print(headers.Fore.GREEN + "1. Mis cursos")
    print(headers.Fore.GREEN + "2. Mis alumnos")
    print(headers.Fore.GREEN + "3. Alumno Conocido")
    print(headers.Fore.RED   + "4. Volver al menú profesor")

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
        else:
            print(headers.Fore.RED + "Opción no válida. Intente de nuevo.")
        menuOpciones()
        opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
    print(headers.Fore.RED + "Volviendo al menú principal...")
    
if __name__ == "__main__":
    menuProfesor(legajoProfesor)