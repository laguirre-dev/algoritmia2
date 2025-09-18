# alumno.py
import entidades.datos # Importamos la base de datos centralizada
 
# Nota: ejemplos de casoso

# CURSOS_DB.append(
#     {"id": "AED1", "nombre": "Algoritmos y Estructuras de Datos I", "profesor": None}
# )
# CURSOS_DB.append({"id": "PROG2", "nombre": "Programación II", "profesor": None})

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

def buscar_alumno_por_legajo(legajo):
    for alumno in ALUMNOS_DB:
        if alumno.get("legajo") == legajo:
            return alumno
    return None


def buscar_curso_por_id(id_curso):
    for curso in CURSOS_DB:
        if curso.get("id") == id_curso:
            return curso
    return None


def verCursosDisponibles():
    if not CURSOS_DB:
        print("No hay cursos disponibles.")
        return
    print("\n--- CURSOS DISPONIBLES ---")
    for curso in CURSOS_DB:
        profesor_nombre = curso.get("profesor") if curso.get("profesor") else "Sin asignar"
        print(f"ID: {curso.get('id')} - {curso.get('nombre')} (Profesor: {profesor_nombre})")


def verMisCursos(legajo):
    alumno = buscar_alumno_por_legajo(legajo)
    if not alumno:
        print("Alumno no encontrado.")
        return
    cursos_inscriptos = alumno.get("cursosInscriptos", [])
    if not cursos_inscriptos:
        print("Aún no estás inscripto en ningún curso.")
        return
    print("\n--- MIS CURSOS ---")
    for id_curso in cursos_inscriptos:
        curso = buscar_curso_por_id(id_curso)
        nombre_curso = curso.get("nombre") if curso else "(curso no encontrado)"
        print(f"{id_curso} - {nombre_curso}")


def inscribirEnCurso(legajo, id_curso):
    # Validar alumno/curso
    alumno = buscar_alumno_por_legajo(legajo)
    if not alumno:
        print(f"Error: No se encontró un alumno con el legajo {legajo}.")
        return False
    curso = buscar_curso_por_id(id_curso)
    if not curso:
        print(f"Error: No se encontró un curso con el ID {id_curso}.")
        return False

    # Asegurar campos esperados
    if "cursosInscriptos" not in alumno:
        alumno["cursosInscriptos"] = []
    if "alumnos" not in curso:
        curso["alumnos"] = []

    # Evitar duplicados
    if id_curso in alumno["cursosInscriptos"]:
        print("Error: Ya estás inscripto en ese curso.")
        return False

    # Guardar en ambos lados 
    alumno["cursosInscriptos"].append(id_curso)
    if alumno.get("legajo") not in curso["alumnos"]:
        curso["alumnos"].append(alumno.get("legajo"))

    print(f"Inscripción exitosa a {curso.get('nombre')}.")
    return True


def darseDeBaja(legajo, id_curso):
    alumno = buscar_alumno_por_legajo(legajo)
    curso = buscar_curso_por_id(id_curso)
    if not alumno or not curso:
        print("Alumno o curso inexistente.")
        return False

    if "cursosInscriptos" not in alumno:
        alumno["cursosInscriptos"] = []
    if "alumnos" not in curso:
        curso["alumnos"] = []

    if id_curso not in alumno["cursosInscriptos"]:
        print("No estabas inscripto en ese curso.")
        return False

    alumno["cursosInscriptos"].remove(id_curso)
    if alumno.get("legajo") in curso["alumnos"]:
        curso["alumnos"].remove(alumno.get("legajo"))

    print(f"Baja exitosa de {curso.get('nombre')}.")
    return True
