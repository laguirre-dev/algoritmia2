"""
Opciones disponibles.
1. Agregar curso
2. Eliminar curso
3. Asignar curso a profesor
4. Generar reporte de cursos
5. Volver al menu Administrativo
"""

from utils import pantalla, validaciones
from . import datos_backup2

# formato
"""
{
    "id": "AED1",
    "nombre": "Algoritmos y Estructuras de Datos I",
    "profesor": 2001,
    "aula": "Aula 101",
    "alumnos": [
        101,
        102
    ]
},
"""


def agregarCurso():
    """
    Crea un diccionario de tipo: Curso y lo agrega a la base de datos de CURSOS_BD
    """
    print("Opcion: Agregar un curso")
    codigo = input("Indique el codigo del curso: ")
    nombre = input("Indique el nombre del curso: ")
    aula = input("Indique el aula del curso: ")
    estructura_curso = {
        "id": codigo,
        "nombre": nombre,
        "profesor": "",
        "aula": aula,
        "alumnos": [],
    }



def eliminarCurso():
    pass


def generarReporteCursos():
    """
    Muestra una tabla con los cursos, sus respectivos profesores y cantidad de alumnos inscriptos
    """
    pass


def asignarCursoAProfesor(legajoProf):
    profesorEncontrado = next(
        (p for p in datos_backup2.PROFESORES_DB if p["legajo"] == legajoProf), None
    )
    if not profesorEncontrado:
        pantalla.redText("Profesor no encontrado.")
        return
    if datos_backup2.CURSOS_DB:
        pantalla.header("CURSOS DISPONIBLES")
        for curso in datos_backup2.CURSOS_DB:
            prof = next(
                (p for p in datos_backup2.PROFESORES_DB if p["legajo"] == curso["profesor"]),
                None,
            )
            nombreProf = (
                f"{prof['nombre']} {prof['apellido']}" if prof else "Sin asignar"
            )
            pantalla.yellowText(
                f"{curso['id']} - {curso['nombre']} (Profesor: {nombreProf})"
            )
        idCurso = input(pantalla.boldText("Ingrese el ID del curso a asignar: "))
        cursoEncontrado = next((c for c in datos_backup2.CURSOS_DB if c["id"] == idCurso), None)
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
