from utils import pantalla as headers
from utils import busquedas as busqueda
from reportes import generador_de_reportes

def generarReporteDeCursosAlumno(legajoAlumno):
    alumno = busqueda.buscarAlumnoPorLegajo(legajoAlumno)
    if alumno is None:
        print(headers.Fore.RED + "Alumno inexistente.")
        return False

    if "cursos" not in alumno or not isinstance(alumno["cursos"], list) or len(alumno["cursos"]) == 0:
        print(headers.Fore.RED + "No estás inscripto en ningún curso.")
        return False

    cursosReporte = []
    for par in alumno["cursos"]:
        if isinstance(par, (list, tuple)) and len(par) >= 2:
            idCurso = par[0]
            estado  = par[1]
            curso = busqueda.buscarCursoPorId(idCurso)
            if curso is not None:
                profesor = busqueda.buscarProfesorPorLegajo(curso["profesor"]) if "profesor" in curso else ""
                item = {
                    "Id": curso["id"] if "id" in curso else str(idCurso),
                    "Nombre": curso["nombre"] if "nombre" in curso else "",
                    "Aula": curso["aula"] if "aula" in curso else "",
                    "Profesor": profesor,
                    "Estado": estado
                }
                cursosReporte.append(item)

    # guarda en /reportes/archivos/alumno_<legajo>_cursos.txt (según tu generador)
    generador_de_reportes.guardarReporte("alumno_" + str(legajoAlumno) + "_cursos", cursosReporte, "txt")
    print(headers.Fore.GREEN + "Reporte generado.")
    return True
