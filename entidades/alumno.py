# alumno.py
from entidades.datos import CURSOS_DB, ALUMNOS_DB, PROFESORES_DB

def menuOpciones():
    print("\n--- MENÚ ALUMNO ---")
    print("1. Inscribirse en un curso")
    print("2. Ver cursos disponibles")
    print("3. Consultar pagos adeudados")
    print("4. Ver estado de aprobación")
    print("5. Volver al menú principal")
    print("6. Ver mis cursos")

def buscarAlumno(legajo):
    return next((alumno for alumno in ALUMNOS_DB if alumno.get("legajo") == legajo), None)

def buscarCurso(id_curso):
    return next((curso for curso in CURSOS_DB if curso.get("id") == id_curso), None)

def buscarProfesor(legajo_prof):
    return next((prof for prof in PROFESORES_DB if prof.get("legajo") == legajo_prof), None)

def verMisCursos(legajo):
    alumno = buscarAlumno(legajo)
    if not alumno or not alumno.get("cursos"):
        print("No estás inscripto en ningún curso.")
        return
    print("\n--- MIS CURSOS ---")
    for idCurso, estado in alumno["cursos"]:
        curso = buscarCurso(idCurso)
        if curso:
            profesor = buscarProfesor(curso["profesor"])
            nombre_prof = f"{profesor['nombre']} {profesor['apellido']}" if profesor else "Sin asignar"
            print(f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']} | Profesor: {nombre_prof} | Estado: {estado}")

def verCursosDisponibles(legajo):
    if not CURSOS_DB:
        print("No hay cursos disponibles.")
        return
    print("\n--- CURSOS DISPONIBLES ---")
    for curso in CURSOS_DB:
        profesor = buscarProfesor(curso.get("profesor"))
        nombre_prof = f"{profesor['nombre']} {profesor['apellido']}" if profesor else "Sin asignar"
        inscripto = " - Inscripto" if legajo in curso.get("alumnos", []) else ""
        print(f"ID: {curso['id']} - {curso['nombre']} (Profesor: {nombre_prof}){inscripto}")

def inscribirEnCurso(legajo, id_curso):
    alumno = buscarAlumno(legajo)
    curso = buscarCurso(id_curso)
    if not alumno or not curso:
        print("Alumno o curso inexistente.")
        return False

    cursos_actuales = set(c[0] for c in alumno["cursos"])
    if id_curso in cursos_actuales:
        print("Error: Ya estás inscripto en ese curso.")
        return False

    alumno["cursos"].append((id_curso, "Desaprobado"))
    curso["alumnos"] = list(set(curso.get("alumnos", [])) | {alumno["legajo"]})

    print(f"Inscripción exitosa a {curso['nombre']}.")
    return True

def darseDeBaja(legajo, id_curso):
    alumno = buscarAlumno(legajo)
    curso = buscarCurso(id_curso)
    if not alumno or not curso:
        print("Alumno o curso inexistente.")
        return False

    cursos_actuales = set(c[0] for c in alumno["cursos"])
    if id_curso not in cursos_actuales:
        print("No estabas inscripto en ese curso.")
        return False

    alumno["cursos"] = [c for c in alumno["cursos"] if c[0] != id_curso]
    curso["alumnos"] = [l for l in curso.get("alumnos", []) if l != legajo]

    print(f"Baja exitosa de {curso['nombre']}.")
    return True

def verEstadoAprobacion(legajo):
    alumno = buscarAlumno(legajo)
    if not alumno or not alumno.get("cursos"):
        print("No tenés cursos inscriptos.")
        return
    print("\n--- ESTADO DE APROBACIÓN ---")
    for idCurso, estado in alumno["cursos"]:
        curso = buscarCurso(idCurso)
        if curso:
            print(f"{curso['id']} - {curso['nombre']} | Estado: {estado}")

def menuAlumno(legajo):
    menuOpciones()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 5:
        if opcion == 1:
            verCursosDisponibles(legajo)
            idCurso = input("Ingrese el ID del curso al que desea inscribirse: ")
            inscribirEnCurso(legajo, idCurso)
        elif opcion == 2:
            verCursosDisponibles(legajo)
        elif opcion == 3:
            print("Consultar pagos adeudados - Funcionalidad en desarrollo.")
        elif opcion == 4:
            verEstadoAprobacion(legajo)
        elif opcion == 6:
            verMisCursos(legajo)
        else:
            print("Opción no válida. Intente de nuevo.")
        menuOpciones()
        opcion = int(input("Seleccione una opción: "))
    print("Volviendo al menú principal...")