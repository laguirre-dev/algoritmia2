from . import datos_backup2 as datos_backup2
from utils import pantalla as headers
from utils import busquedas as busqueda

def verMisCursos(legajo):
    alumno = busqueda.buscarAlumnoPorLegajo(legajo)
    if not alumno or not alumno.get("cursos"):
        print(headers.Fore.RED + "No estás inscripto en ningún curso.")
        return

    headers.header("MIS CURSOS")
    for idCurso, estado in alumno["cursos"]:
        curso = busqueda.buscarCursoPorId(idCurso)
        if curso:
            profesor = busqueda.buscarProfesorPorLegajo(curso.get("profesor"))
            colorEstado = headers.Fore.GREEN if estado == "Aprobado" else headers.Fore.RED
            print(
                headers.Fore.WHITE
                + f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']} | Profesor: {profesor} | Estado: "
                + colorEstado
                + estado
            )

def verCursosDisponibles(legajo):
    if not datos_backup2.CURSOS_DB:
        print(headers.Fore.RED + "No hay cursos disponibles.")
        return

    headers.header("CURSOS DISPONIBLES")
    for curso in datos_backup2.CURSOS_DB:
        profesor = busqueda.buscarProfesorPorLegajo(curso.get("profesor"))
        inscripto = headers.Fore.GREEN + " (Inscripto)" if legajo in curso.get("alumnos", []) else ""
        print(
            headers.Fore.WHITE
            + f"ID: {curso['id']} - {curso['nombre']} (Profesor: {profesor})"
            + inscripto
        )

def verEstadoAprobacion(legajo):
    alumno = busqueda.buscarAlumnoPorLegajo(legajo)
    if not alumno or not alumno.get("cursos"):
        print(headers.Fore.RED + "No tenés cursos inscriptos.")
        return

    headers.header("ESTADO DE APROBACIÓN")
    for idCurso, estado in alumno["cursos"]:
        curso = busqueda.buscarCursoPorId(idCurso)
        if curso:
            colorEstado = headers.Fore.GREEN if estado == "Aprobado" else headers.Fore.RED
            print(
                headers.Fore.WHITE
                + f"{curso['id']} - {curso['nombre']} | Estado: "
                + colorEstado
                + estado
            )