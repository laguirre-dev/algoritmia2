from entidades import datos as datos
from utils import pantalla as headers
from utils import busquedas as busqueda
from reportes import generador_de_reportes  
from datetime import datetime

def diaDeExamen(legajoProfesor):
    profesor = busqueda.buscarProfesorPorLegajo(legajoProfesor)
    cursosProfesor = list(filter(lambda c: c.get("profesor") == legajoProfesor, datos.sistema["CURSOS_BD"]))
    
    if not profesor:
        print(headers.Fore.RED + "Profesor inexistente.")
        return False
    elif not cursosProfesor:
        print(headers.Fore.RED + "No tenés cursos asignados.")
        return False

    # Mostrar cursos disponibles
    headers.header("DÍA DE EXAMEN - SELECCIÓN DE CURSO")
    headers.header("MIS CURSOS")
    for curso in cursosProfesor:
        print(headers.Fore.WHITE + f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']}")

    idCurso = input(headers.Fore.WHITE + "\nIngrese el ID del curso que desea gestionar: ").upper()
    curso = busqueda.buscarCursoPorId(idCurso)

    if not curso or curso.get("profesor") != legajoProfesor:
        print(headers.Fore.RED + "Curso no válido o no pertenece a este profesor.")
        return False


    if not curso.get("alumnos"):
        print(headers.Fore.RED + "No hay alumnos inscriptos en este curso.")
        return False
    
    alumnosEvaluados = []
    for legajoAlumno in curso.get("alumnos", []):   
        alumno = busqueda.buscarAlumnoPorLegajo(legajoAlumno)
        if alumno:
            alumno["cursos"] = [
                (c[0], "Aprobado" if c[0] == idCurso else c[1]) for c in alumno["cursos"]
            ]
            alumnosEvaluados.append({
                "legajo": alumno["legajo"],
                "nombre": alumno["nombre"],
                "apellido": alumno["apellido"],
                "curso": curso["nombre"],   
                "estado": "Aprobado"
            })

    # Generar reporte del día de Examen
    fecha = datetime.now().strftime("%Y%m%d")
    nombreReporte = f"Evaluados_{fecha}_{legajoProfesor}"
    try:
        generador_de_reportes.guardarReporte(nombreReporte, alumnosEvaluados)
        print(headers.Fore.GREEN + f"Reporte '{nombreReporte}' generado correctamente.")
        return True
    except Exception as e:
        print(headers.Fore.RED + f"Error al generar el reporte: {e}")
        return False
