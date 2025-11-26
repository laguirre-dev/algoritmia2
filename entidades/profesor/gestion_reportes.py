from entidades import datos as datos
from utils import pantalla as headers
from utils import busquedas as busqueda
from reportes import generador_de_reportes  

def generarReporteDeCursosAlumno(legajoProfesor):
    cursosProfesor = [c for c in datos.sistema["CURSOS_BD"] if c["profesor"] == legajoProfesor]
    alumnosSet = set()
    for curso in cursosProfesor:
        alumnosSet.update(curso.get("alumnos", []))

    alumnosReporte = []
    for legajo in alumnosSet:
        alumno = busqueda.buscarAlumnoPorLegajo(legajo)
        if alumno:
            alumnosReporte.append({
                "legajo": alumno["legajo"],
                "nombre": alumno["nombre"],
                "apellido": alumno["apellido"],
                "cursos": [idC for (idC, _) in alumno["cursos"]]
            })

    generador_de_reportes.guardarReporte(f"alumnos_{legajoProfesor}", alumnosReporte)


def generarReporteDeAlumnosAprobados(legajoProfesor):
    cursosProfesor = [c for c in datos.sistema["CURSOS_BD"] if c["profesor"] == legajoProfesor]
    alumnosAprobados = []

    for curso in cursosProfesor:
        for legajo in curso.get("alumnos", []):
            alumno = busqueda.buscarAlumnoPorLegajo(legajo)
            if alumno:
                for idC, estado in alumno["cursos"]:
                    if idC == curso["id"] and estado == "Aprobado":
                        alumnosAprobados.append({
                            "legajo": alumno["legajo"],
                            "nombre": alumno["nombre"],
                            "apellido": alumno["apellido"],
                            "curso": idC
                        })

    generador_de_reportes.guardarReporte(f"aprobados_{legajoProfesor}", alumnosAprobados)


def generarReporteDeCursos(legajoProfesor):
    cursosProfesor = [c for c in datos.sistema["CURSOS_BD"] if c["profesor"] == legajoProfesor]

    cursosReporte = []
    for curso in cursosProfesor:
        cursosReporte.append({
            "id": curso["id"],
            "nombre": curso["nombre"],
            "aula": curso["aula"],
            "cantidad alumnos": len(curso.get("alumnos", []))
        })

    generador_de_reportes.guardarReporte(f"cursos_{legajoProfesor}", cursosReporte)