# administrativo.py

def menu_administrativo():
    """Muestra el menú de opciones para un Administrativo."""
    print("\n--- MENÚ ADMINISTRATIVO ---")
    print("1. Asignar cursos y aulas a profesores")
    print("2. Aprobar pagos de alumnos")
    print("3. Volver al menú principal")

    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Asignar cursos y aulas - Funcionalidad en desarrollo.")
        elif opcion == '2':
            print("Aprobar pagos - Funcionalidad en desarrollo.")
        elif opcion == '3':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")