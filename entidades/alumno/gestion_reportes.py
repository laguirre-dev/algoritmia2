from entidades import datos as datos
from utils import pantalla as headers
from utils import busquedas as busqueda
from reportes import generador_de_reportes  

def generarReporteDeCursosAlumno(legajoAlumno):
    alumno = busqueda.buscarAlumnoPorLegajo(legajoAlumno)
    if not alumno:
        print(headers.Fore.RED + "Alumno inexistente.")
        return False

    if not alumno.get("cursos"):
        print(headers.Fore.RED + "No estás inscripto en ningún curso.")
        return False

    cursosReporte = []
    for idCurso, estado in alumno["cursos"]:
        curso = busqueda.buscarCursoPorId(idCurso)
        if curso:
            profesor = busqueda.buscarProfesorPorLegajo(curso.get("profesor"))
            cursosReporte.append({
                "Id": curso["id"],
                "Nombre": curso["nombre"],
                "Aula": curso["aula"],
                "Profesor": profesor,
                "Estado": estado
            })
            
    generador_de_reportes.guardarReporte(f"alumno_{legajoAlumno}_cursos", cursosReporte, "txt")

