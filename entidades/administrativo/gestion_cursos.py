"""
Opciones disponibles.
1. Agregar curso
2. Eliminar curso
3. Asignar curso a profesor
4. Generar reporte de cursos
5. Volver al menu Administrativo
"""

from utils import pantalla, validaciones
from entidades import datos


def agregarCurso():
    pass


def eliminarCurso():
    pass


def generarReporteCursos():
    """
    Muestra una tabla con los cursos, sus respectivos profesores y cantidad de alumnos inscriptos
    """
    pass


def asignarCursoAProfesor(legajoProf):
    profesorEncontrado = next(
        (p for p in datos.PROFESORES_DB if p["legajo"] == legajoProf), None
    )
    if not profesorEncontrado:
        pantalla.redText("Profesor no encontrado.")
        return
    if datos.CURSOS_DB:
        pantalla.header("CURSOS DISPONIBLES")
        for curso in datos.CURSOS_DB:
            prof = next(
                (p for p in datos.PROFESORES_DB if p["legajo"] == curso["profesor"]),
                None,
            )
            nombreProf = (
                f"{prof['nombre']} {prof['apellido']}" if prof else "Sin asignar"
            )
            pantalla.yellowText(
                f"{curso['id']} - {curso['nombre']} (Profesor: {nombreProf})"
            )
        idCurso = input(pantalla.boldText("Ingrese el ID del curso a asignar: "))
        cursoEncontrado = next((c for c in datos.CURSOS_DB if c["id"] == idCurso), None)
        if not cursoEncontrado:
            pantalla.redText("Curso no encontrado.")
            return
        cursoEncontrado["profesor"] = profesorEncontrado["legajo"]
        if cursoEncontrado["id"] not in profesorEncontrado["materias"]:
            profesorEncontrado["materias"].append(cursoEncontrado["id"])
        pantalla.greenText(
            f"Curso {cursoEncontrado['nombre']} asignado al profesor {profesorEncontrado['nombre']}."
        )
    else:
        pantalla.redText(
            "No hay cursos disponibles. Por favor ingresar un curso primero."
        )
        return


logica_seleccion_menu = {
    1: agregarCurso,
    2: eliminarCurso,
    3: asignarCursoAProfesor,
    4: generarReporteCursos,
}


def menuGestionCursos():
    """Muestra el menu de opciones de un Administrativo en la gestion de cursos"""
    pantalla.opcionesAdministrativoCursos()
    opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    try:
        while opcion != 0:
            logica_seleccion_menu[opcion]()
            pantalla.opcionesAdministrativoCursos()
            opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    except Exception as e:
        print(e)
    return
