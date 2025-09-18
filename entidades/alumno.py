# alumno.py
from entidades.datos import CURSOS_DB, ALUMNOS_DB  # Importamos la base de datos centralizada
 
def menu_opciones():
    print("\n--- MENÚ ALUMNO ---")
    print("\n1. Inscribirse en un curso")
    print("2. Ver cursos disponibles")
    print("3. Consultar pagos adeudados")
    print("4. Ver estado de aprobación")
    print("5. Volver al menú principal")

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


def verCursosDisponibles(legajo):
    if not CURSOS_DB:
        print("No hay cursos disponibles.")
        return
    print("\n--- CURSOS DISPONIBLES ---")
    for curso in CURSOS_DB:
        profesor_nombre = curso.get("profesor") if curso.get("profesor") else "Sin asignar"
        # imprimir "inscripto" si el alumno esta inscripto
        if legajo in curso.get("alumnos", []):
            print(f"ID: {curso.get('id')} - {curso.get('nombre')} (Profesor: {profesor_nombre}) - Inscripto")
        else:
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

def menuAlumno(legajo):
    """Muestra y gestiona el menú de opciones para un Alumno."""
    # Aquí iría la lógica para validar el usuario. Agregar en un futuro.
    legajoIngresado = 101  # Asumimos que el legajo es 101 para la prueba
    menu_opciones()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 5:
        if opcion == 1:
            verCursosDisponibles(legajo)
            idCurso = input("Ingrese el ID del curso al que desea inscribirse: ")
            inscribirEnCurso(legajoIngresado, idCurso)
        elif opcion == 2:
            verCursosDisponibles(legajo)
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