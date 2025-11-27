"""
Opciones disponibles.
1. Agregar curso
2. Eliminar curso
3. Asignar curso a profesor
4. Generar reporte de cursos
5. Volver al menu Administrativo
"""

from utils import pantalla, validaciones
from reportes import generador_de_reportes
from entidades.administrativo import menuAdministrativo
from datetime import date
from entidades import datos
from tabulate import tabulate


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
    try:
        datos.CURSOS_DB.append(estructura_curso)
    except Exception as e:
        print(e)
        return False
    return True


def eliminarCurso():
    """
    Elimina un curso de la base de datos. Pide el id del curso
    """
    codigo = input("Indique el codigo del curso a eliminar: ")
    eliminado = False
    for curso in datos.CURSOS_DB:
        if curso["id"] == codigo:
            datos.CURSOS_DB.remove(curso)
            eliminado = True
    if not eliminado:
        print(f"El curso {codigo} no fue encontrado.")
    else:
        print(f"El curso {codigo} fue eliminado con exito.")


def generarReporteCursos():
    """
    Muestra una tabla con los cursos, sus respectivos profesores y cantidad de alumnos inscriptos. Guardamos el reporte en un archivo .txt
    """
    print("Opcion: Generar reporte de cursos")
    cursos = [
        [curso["id"], curso["nombre"], curso["profesor"], len(curso["alumnos"])]
        for curso in datos.CURSOS_DB
    ]
    print(tabulate(cursos, headers=["Codigo", "Nombre", "Profesor", "Alumnos"]))
    fecha = date.today()
    nombre_archivo = f"reporte_cursos_{fecha}"
    generador_de_reportes.guardarReporte(nombre_archivo, cursos)
    return


def asignarCursoAProfesor(legajoProf):
    """
    Realiza la modificacion del campo Profesor en el Curso segun el Legajo y el codigo del curso
    """
    try:
        legajoProf = int(input("Ingrese el legajo del profesor: "))
    except ValueError:
        print("Introdujo un legajo no valido. Debe ser numerico.")
        return
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
    5: menuAdministrativo,
}


def menuGestionCursos():
    """Muestra el menu de opciones de un Administrativo en la gestion de cursos"""
    pantalla.opcionesAdministrativoCursos()
    opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    while opcion != 0:
        logica_seleccion_menu[opcion]()
        pantalla.opcionesAdministrativoCursos()
        opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    return
