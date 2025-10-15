from entidades.datos import CURSOS_DB, ALUMNOS_DB, PROFESORES_DB
from colorama import init, Fore, Style

# Inicializamos colorama
init(autoreset=True)

def header(titulo):
    # Encabezado estilizado con onda universitaria
    print(Fore.GREEN + "=" * 50)
    print(Style.BRIGHT + Fore.WHITE + titulo.center(50))
    print(Fore.GREEN + "=" * 50)

def menuOpciones():
    print("\n")
    header("MENÚ ALUMNO")
    print(Fore.GREEN + "1. Inscribirse en un curso")
    print(Fore.GREEN + "2. Ver cursos disponibles")
    print(Fore.GREEN + "3. Consultar pagos adeudados")
    print(Fore.GREEN + "4. Ver estado de aprobación")
    print(Fore.GREEN + "5. Ver mis cursos")
    print(Fore.RED   + "6. Volver al menú principal")
    

def buscarAlumnoPorLegajo(legajo):
    return next((alumno for alumno in ALUMNOS_DB if alumno.get("legajo") == legajo), None)

def buscarCursoPorId(idCurso):
    return next((curso for curso in CURSOS_DB if curso.get("id") == idCurso), None)

def buscarProfesorPorLegajo(legajoProf):
    return next((prof for prof in PROFESORES_DB if prof.get("legajo") == legajoProf), None)

def verMisCursos(legajo):
    alumno = buscarAlumnoPorLegajo(legajo)
    if not alumno or not alumno.get("cursos"):
        print(Fore.RED + "No estás inscripto en ningún curso.")
        return
    header("MIS CURSOS")
    for idCurso, estado in alumno["cursos"]:
        curso = buscarCursoPorId(idCurso)
        if curso:
            profesor = buscarProfesorPorLegajo(curso["profesor"])
            nombreProf = f"{profesor['nombre']} {profesor['apellido']}" if profesor else "Sin asignar"
            colorEstado = Fore.GREEN if estado == "Aprobado" else Fore.RED
            print(Fore.WHITE + f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']} | Profesor: {nombreProf} | Estado: " + colorEstado + estado)

def verCursosDisponibles(legajo):
    if not CURSOS_DB:
        print(Fore.RED + "No hay cursos disponibles.")
        return
    header("CURSOS DISPONIBLES")
    for curso in CURSOS_DB:
        profesor = buscarProfesorPorLegajo(curso.get("profesor"))
        nombreProf = f"{profesor['nombre']} {profesor['apellido']}" if profesor else "Sin asignar"
        inscripto = Fore.GREEN + " (Inscripto)" if legajo in curso.get("alumnos", []) else ""
        print(Fore.WHITE + f"ID: {curso['id']} - {curso['nombre']} (Profesor: {nombreProf})" + inscripto)

def inscribirEnCurso(legajo, idCurso):
    alumno = buscarAlumnoPorLegajo(legajo)
    curso = buscarCursoPorId(idCurso)
    if not alumno or not curso:
        print(Fore.RED + "Alumno o curso inexistente.")
        return False

    cursosActuales = set(c[0] for c in alumno["cursos"])
    if idCurso in cursosActuales:
        print(Fore.RED + "Error: Ya estás inscripto en ese curso.")
        return False

    alumno["cursos"].append((idCurso, "Desaprobado"))
    curso["alumnos"] = list(set(curso.get("alumnos", [])) | {alumno["legajo"]})

    print(Fore.GREEN + f"Inscripción exitosa a {curso['nombre']}.")
    return True

def darseDeBaja(legajo, idCurso):
    alumno = buscarAlumnoPorLegajo(legajo)
    curso = buscarCursoPorId(idCurso)
    if not alumno or not curso:
        print(Fore.RED + "Alumno o curso inexistente.")
        return False

    cursosActuales = set(c[0] for c in alumno["cursos"])
    if idCurso not in cursosActuales:
        print(Fore.RED + "No estabas inscripto en ese curso.")
        return False

    alumno["cursos"] = [c for c in alumno["cursos"] if c[0] != idCurso]
    curso["alumnos"] = [l for l in curso.get("alumnos", []) if l != legajo]

    print(Fore.GREEN + f"Baja exitosa de {curso['nombre']}.")
    return True

def verEstadoAprobacion(legajo):
    alumno = buscarAlumnoPorLegajo(legajo)
    if not alumno or not alumno.get("cursos"):
        print(Fore.RED + "No tenés cursos inscriptos.")
        return
    header("ESTADO DE APROBACIÓN")
    for idCurso, estado in alumno["cursos"]:
        curso = buscarCursoPorId(idCurso)
        if curso:
            colorEstado = Fore.GREEN if estado == "Aprobado" else Fore.RED
            print(Fore.WHITE + f"{curso['id']} - {curso['nombre']} | Estado: " + colorEstado + estado)

def menuAlumno(legajo):
    """Muestra y gestiona el menú de opciones para un Alumno."""
    menuOpciones()
    opcion = int(input(Fore.WHITE + "Seleccione una opción: "))
    while opcion != 6:
        if opcion == 1:


            verCursosDisponibles(legajo)
            idCurso = input(Fore.WHITE + "Ingrese el ID del curso al que desea inscribirse: ")
            inscribirEnCurso(legajo, idCurso)

        elif opcion == 2:
            verCursosDisponibles()
        elif opcion == 3:
            print(Fore.GREEN + "Consultar pagos adeudados - Funcionalidad en desarrollo.")
        elif opcion == 4:
            verEstadoAprobacion(legajo)
        elif opcion == 5:
            verMisCursos(legajo)
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")
        menuOpciones()
        opcion = int(input(Fore.WHITE + "Seleccione una opción: "))
    print(Fore.RED + "Volviendo al menú principal...")