# main.py
from entidades.alumno import menuAlumno
from entidades.profesor import menu_profesor
from entidades.administrativo import menu_administrativo


def mostrarMenu():
    """Muestra el menú principal."""
    print("---------------------------------")
    print("SISTEMA DE GESTIÓN DE ALUMNOS")
    print("---------------------------------")
    print("1. Iniciar sesión como Alumno")
    print("2. Iniciar sesión como Profesor")
    print("3. Iniciar sesión como Administrativo")
    print("4. Salir")
    print("---------------------------------")


def main():
    """Función principal del programa."""
    mostrarMenu()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 4:
        if opcion == 1:
            menuAlumno()
        elif opcion == 2:
            menu_profesor()
        elif opcion == 3:
            menu_administrativo()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        mostrarMenu()
        opcion = int(input("Seleccione una opción: "))
    print("Saliendo del sistema...")
    # Le agrego esto para mostrar el mensaje de salida
    input("Presione Enter para salir")


main()
