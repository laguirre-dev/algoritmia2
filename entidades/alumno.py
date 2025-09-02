# alumno.py

# Esta es la base de datos de alumnos y cursos. Por ahora, son listas vacías. En el futuro, cargaremos y guardaremos estos datos en archivos.
ALUMNOS_DB = []
CURSOS_DB = []
PROFESORES_DB = []

# Nota: ejemplos de casoso

CURSOS_DB.append({"id": "AED1", "nombre": "Algoritmos y Estructuras de Datos I", "profesor": None})
CURSOS_DB.append({"id": "PROG2", "nombre": "Programación II", "profesor": None})

def registrarAlumno(legajo, nombre):
    """
    Registra un nuevo alumno en la base de datos.
    Verifica que el legajo no exista antes de agregarlo.
    """
    for alumno in ALUMNOS_DB:
        if alumno["legajo"] == legajo:
            print(f"Error: El legajo {legajo} ya está registrado.")
            return False

    nuevoAlumno = {
        "legajo": legajo,
        "nombre": nombre,
        "cursosInscriptos": [],
        "pagosAdeudados": False,
        "estadoAprobacion": "Desaprobado"
    }
    ALUMNOS_DB.append(nuevoAlumno)
    print(f"Alumno {nombre} con legajo {legajo} registrado con éxito.")
    return True

def verCursosDisponibles():
    """Muestra la lista de cursos disponibles."""
    if not CURSOS_DB:
        print("No hay cursos disponibles en este momento.")
        return

    print("\n--- CURSOS DISPONIBLES ---")
    for curso in CURSOS_DB:
        print(f"ID: {curso['id']} - Nombre: {curso['nombre']} - Profesor: {curso['profesor']}")

def inscribirEnCurso(legajo, idCurso):
    """
    Inscribe a un alumno en un curso.
    """
    alumnoEncontrado = None
    for alumno in ALUMNOS_DB:
        if alumno["legajo"] == legajo:
            alumnoEncontrado = alumno
            break

    if not alumnoEncontrado:
        print(f"Error: No se encontró un alumno con el legajo {legajo}.")
        return False

    cursoEncontrado = None
    for curso in CURSOS_DB:
        if curso["id"] == idCurso:
            cursoEncontrado = curso
            break

    if not cursoEncontrado:
        print(f"Error: No se encontró un curso con el ID {idCurso}.")
        return False

    if idCurso in alumnoEncontrado["cursosInscriptos"]:
        print(f"Error: El alumno ya está inscripto en este curso.")
        return False

    alumnoEncontrado["cursosInscriptos"].append(idCurso)
    print(f"Alumno {alumnoEncontrado['nombre']} inscripto en el curso {cursoEncontrado['nombre']} con éxito.")
    return True


def menuAlumno():
    """Muestra y gestiona el menú de opciones para un Alumno."""
    print("\n--- MENÚ ALUMNO ---")
    
    # Aquí iría la lógica para validar el usuario. Agregar en un futuro.
    registrarAlumno(101, "Sofia Perez")
    
    legajoIngresado = 101 # Asumimos que el legajo es 101 para la prueba

    while True:
        print("\n1. Inscribirse en un curso")
        print("2. Ver cursos disponibles")
        print("3. Consultar pagos adeudados")
        print("4. Ver estado de aprobación")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            verCursosDisponibles()
            idCurso = input("Ingrese el ID del curso al que desea inscribirse: ")
            inscribirEnCurso(legajoIngresado, idCurso)
        elif opcion == '2':
            verCursosDisponibles()
        elif opcion == '3':
            # Funcionalidad en desarrollo
            print("Consultar pagos adeudados - Funcionalidad en desarrollo.")
        elif opcion == '4':
            # Funcionalidad en desarrollo
            print("Ver estado de aprobación - Funcionalidad en desarrollo.")
        elif opcion == '5':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")