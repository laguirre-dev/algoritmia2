# administrativo.py
def menu_opciones():
    print("\n--- MENÚ ADMINISTRATIVO ---")
    print("1. Asignar cursos y aulas a profesores")
    print("2. Aprobar pagos de alumnos")
    print("3. Volver al menú principal")

# Prueba


def menu_administrativo():
    """Muestra el menú de opciones para un Administrativo."""
    # Comentario de Fede a modo de prueba
    menu_opciones()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 3:
        if opcion == 1:
            print("Asignar cursos y aulas - Funcionalidad en desarrollo.")
        elif opcion == 2:
            print("Aprobar pagos - Funcionalidad en desarrollo.")
        else:
            print("Opción no válida. Intente de nuevo.")
        menu_opciones()
        opcion = int(input("Seleccione una opción: "))
    print("Volviendo al menú principal...")

# funcion Dar de alta Alumno: Legajo y Clave
# funcion Dar de Alta Profesor: Legajo y Clave
# funcion Asignar Materia a Profesor

