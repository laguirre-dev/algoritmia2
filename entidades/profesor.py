# profesor.py
def menu_opciones():
    print("\n--- MENÚ PROFESOR ---")
    print("1. Visualizar cursos y aulas")
    print("2. Aprobar o desaprobar alumnos")
    print("3. Volver al menú principal")


def menu_profesor():
    """Muestra el menú de opciones para un Profesor."""
    menu_opciones()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 3:
        if opcion == 1:
            print("Visualizar cursos y aulas - Funcionalidad en desarrollo.")
        elif opcion == 2:
            print("Aprobar o desaprobar alumnos - Funcionalidad en desarrollo.")
        else:
            print("Opción no válida. Intente de nuevo.")
        menu_opciones()
        opcion = int(input("Seleccione una opción: "))
    print("Volviendo al menú principal...")
