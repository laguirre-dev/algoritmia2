# profesor.py

def menu_profesor():
    """Muestra el menú de opciones para un Profesor."""
    print("\n--- MENÚ PROFESOR ---")
    print("1. Visualizar cursos y aulas")
    print("2. Aprobar o desaprobar alumnos")
    print("3. Volver al menú principal")

    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Visualizar cursos y aulas - Funcionalidad en desarrollo.")
        elif opcion == '2':
            print("Aprobar o desaprobar alumnos - Funcionalidad en desarrollo.")
        elif opcion == '3':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")