import entidades.datos as datos
import utils.pantalla as headers
import utils.busquedas as buscar

def inscribirEnCurso(legajo, idCurso):
    alumno = buscar.buscarAlumnoPorLegajo(legajo)
    curso = buscar.buscarCursoPorId(idCurso)
    if not alumno or not curso:
        print(headers.Fore.RED + "Alumno o curso inexistente.")
        return False

    cursosActuales = set(c[0] for c in alumno["cursos"])
    if idCurso in cursosActuales:
        print(headers.Fore.RED + "Error: Ya estás inscripto en ese curso.")
        return False

    alumno["cursos"].append((idCurso, "Desaprobado"))
    curso["alumnos"] = list(set(curso.get("alumnos", [])) | {alumno["legajo"]})

    print(headers.Fore.GREEN + f"Inscripción exitosa a {curso['nombre']}.")
    return True

def darseDeBaja(legajo, idCurso):
    alumno = buscar.buscarAlumnoPorLegajo(legajo)
    curso = buscar.buscarCursoPorId(idCurso)
    if not alumno or not curso:
        print(headers.Fore.RED + "Alumno o curso inexistente.")
        return False

    cursosActuales = set(c[0] for c in alumno["cursos"])
    if idCurso not in cursosActuales:
        print(headers.Fore.RED + "No estabas inscripto en ese curso.")
        return False

    alumno["cursos"] = [c for c in alumno["cursos"] if c[0] != idCurso]
    curso["alumnos"] = [l for l in curso.get("alumnos", []) if l != legajo]

    print(headers.Fore.GREEN + f"Baja exitosa de {curso['nombre']}.")
    return True