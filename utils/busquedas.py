from entidades import datos
from utils import pantalla as headers

def validaCredenciales(legajo, clave):
    for credencial in datos.sistema["CREDENCIALES"]:
        if clave == credencial["clave"] and legajo == credencial["legajo"]:
            return credencial["rol"]
    return None

def buscarAlumnoPorLegajo(legajo):
    for alumno in datos.sistema["ALUMNOS_BD"]:
        if alumno["legajo"] == legajo:
            return alumno
    return None

def buscarAlumnoPorLegajoNombreYApellido(legajo):
    for alumno in datos.sistema["ALUMNOS_BD"]:
        if alumno["legajo"] == legajo:
            return f"{alumno['nombre']} {alumno['apellido']}"
    return f"Alumno con legajo {legajo} no encontrado"

def buscarProfesorPorLegajo(legajo_profesor):
    for profesor in datos.sistema["PROFESORES_BD"]:
        if profesor["legajo"] == legajo_profesor:
            return f"{profesor['nombre']} {profesor['apellido']}"
    return f"Profesor con legajo {legajo_profesor} no encontrado"

def buscarCursoPorId(idCurso):
    for curso in datos.sistema["CURSOS_BD"]:
        if curso["id"] == idCurso:
            return curso
    return None

def validarAlumnoYCurso(legajo, idCurso):
    alumno = buscarAlumnoPorLegajo(legajo)
    curso = buscarCursoPorId(idCurso)
    if not alumno or not curso:
        print(headers.Fore.RED + "Alumno o curso inexistente.")
        return None, None
    return alumno, curso