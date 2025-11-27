"""
El objetivo del modulo es centralizar las funciones reutilizables para usarlas en cualquier parte de las funciones
1. Buscar alumno
2. Buscar profesor
3. Buscar materia
4. Buscar pagos

Las funciones deben devolver el contenido de la entidad filtrada: Por ej, detalles del alumno, materia, pago (alumno, monto, vencimiento, etc)
"""

from . import datos_backup2 as datos_backup2
from utils import pantalla as headers

def validaCredenciales(legajo, clave):
    for credencial in datos_backup2.CREDENCIALES:
        if clave == credencial["clave"] and legajo == credencial["legajo"]:
            return credencial["rol"]
    return None

def buscaCredenciales():
    for credencial in datos_backup2.CREDENCIALES:
        print(f"Legajo: {credencial["legajo"]}, Clave: {credencial["clave"]}, Rol: {credencial["rol"]}")


def buscarAlumnoPorLegajo(legajo):
    """
    Busca un alumno en ALUMNOS_DB por legajo. Retorna el diccionario del alumno si lo encuentra, o None si no existe.
    """
    for alumno in datos_backup2.ALUMNOS_DB:
        if alumno["legajo"] == legajo:
            return alumno
    return None


def buscarAlumnoPorLegajoNombreYApellido(legajo):
    for alumno in datos_backup2.ALUMNOS_DB:
        if alumno["legajo"] == legajo:
            return f"{alumno['nombre']} {alumno['apellido']}"
    return f"Alumno con legajo {legajo} no encontrado"


def validarAlumnoYCurso(legajo, idCurso):
    alumno = buscarAlumnoPorLegajo(legajo)
    curso = buscarCursoPorId(idCurso)
    if not alumno or not curso:
        print(headers.Fore.RED + "Alumno o curso inexistente.")
        return None, None
    return alumno, curso


def buscarProfesorPorLegajo(legajo_profesor):
    """
    Busca un profesor en PROFESORES_DB por legajo. Retorna el nombre completo si lo encuentra, o un mensaje si no existe.
    """
    for profesor in datos_backup2.PROFESORES_DB:
        if profesor["legajo"] == legajo_profesor:
            return f"{profesor['nombre']} {profesor['apellido']}"
    return f"Profesor con legajo {legajo_profesor} no encontrado"


def buscarMateria():
    print("En desarrollo...")
    return None


def buscarCursoPorId(idCurso):
    """
    Busca un curso en CURSOS_DB por id. Retorna el diccionario del curso si lo encuentra, o None si no existe.
    """
    for curso in datos_backup2.CURSOS_DB:
        if curso["id"] == idCurso:
            return curso
    return None


def buscarPagos():
    print("En desarrollo...")
    return
