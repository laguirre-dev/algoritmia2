import datos  # Importamos la base de datos centralizada

def registrarAlumno(legajo, nombre):
    """
    Registra un nuevo alumno en la base de datos.
    Verifica que el legajo no exista antes de agregarlo.
    """
    for alumno in datos.ALUMNOS_DB:
        if alumno["legajo"] == legajo:
            print(f"Error: El legajo {legajo} ya está registrado.")
            return False

    nuevoAlumno = {
        "legajo": legajo,
        "nombre": nombre,
        "cursosInscriptos": [],
        "pagosAdeudados": False,
        "estadoAprobacion": "Desaprobado",
    }
    datos.ALUMNOS_DB.append(nuevoAlumno)
    print(f"Alumno {nombre} con legajo {legajo} registrado con éxito.")
    return True


def verCursosDisponibles():
    return True


def inscribirEnCurso(legajo, idCurso):
    return True


def menu_opciones():
    print("\n--- MENÚ ALUMNO ---")
    print("\n1. Inscribirse en un curso")
    print("2. Ver cursos disponibles")
    print("3. Consultar pagos adeudados")
    print("4. Ver estado de aprobación")
    print("5. Volver al menú principal")


def menuAlumno():
    """Muestra y gestiona el menú de opciones para un Alumno."""
    # Aquí iría la lógica para validar el usuario. Agregar en un futuro.
    registrarAlumno(101, "Sofia Perez")
    legajoIngresado = 101  # Asumimos que el legajo es 101 para la prueba
    menu_opciones()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 5:
        if opcion == 1:
            verCursosDisponibles()
            idCurso = input("Ingrese el ID del curso al que desea inscribirse: ")
            inscribirEnCurso(legajoIngresado, idCurso)
        elif opcion == 2:
            verCursosDisponibles()
        elif opcion == 3:
            # Funcionalidad en desarrollo
            print("Consultar pagos adeudados - Funcionalidad en desarrollo.")
        elif opcion == 4:
            # Funcionalidad en desarrollo
            print("Ver estado de aprobación - Funcionalidad en desarrollo.")
        else:
            print("Opción no válida. Intente de nuevo.")
        menu_opciones()
        opcion = int(input("Seleccione una opción: "))
    print("Volviendo al menú principal...")


# funcion para que el Alumno se inscriba a una materia existente



