from entidades import datos as datos
from utils import pantalla as headers
from utils import busquedas as busqueda

def verMisCursos(legajoProfesor):
    cursosProfesor = list(filter(lambda c: c.get("profesor") == legajoProfesor, datos.sistema["CURSOS_BD"]))
    if not cursosProfesor:
        print(headers.Fore.RED + "No tenés cursos asignados.")
        return
    headers.header("MIS CURSOS")
    for curso in cursosProfesor:
        print(headers.Fore.WHITE + f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']}")

def verMisAlumnos(legajoProfesor):
    cursosProfesor = list(filter(lambda c: c.get("profesor") == legajoProfesor, datos.sistema["CURSOS_BD"]))
    if not cursosProfesor:
        print(headers.Fore.RED + "No tenés cursos asignados.")
        return

    headers.header("MIS ALUMNOS")

    alumnosSet = set()
    for curso in cursosProfesor:
        alumnosSet.update(curso.get("alumnos", []))

    if not alumnosSet:
        print(headers.Fore.RED + "No hay alumnos inscriptos en tus cursos.")
        return

    for legajo in alumnosSet:
        alumno = busqueda.buscarAlumnoPorLegajo(legajo)
        if alumno:
            estados = [(idC, estado) for (idC, estado) in alumno["cursos"] if any(c["id"] == idC for c in cursosProfesor)]
            estadosStr = ", ".join([f"{idC}: {estado}" for idC, estado in estados])
            print(headers.Fore.WHITE + f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']} | Cursos: {estadosStr}")
            
def alumnoConocido(legajoProfesor):
    cursosProfesor = [c for c in datos.sistema["CURSOS_BD"] if c.get("profesor") == legajoProfesor]
    if not cursosProfesor:
        print(headers.Fore.RED + "No tenés cursos asignados.")
        return

    conjuntosAlumnos = [set(curso.get("alumnos", [])) for curso in cursosProfesor if curso.get("alumnos")]

    if len(conjuntosAlumnos) < 2:
        print(headers.Fore.RED + "No hay alumnos que estén en dos o más cursos.")
        return

    alumnosConocidos = set()
    for i in range(len(conjuntosAlumnos)):
        for j in range(i + 1, len(conjuntosAlumnos)):
            alumnosConocidos |= (conjuntosAlumnos[i] & conjuntosAlumnos[j])

    headers.header("ALUMNOS CONOCIDOS")
    if not alumnosConocidos:
        print(headers.Fore.RED + "No hay alumnos que estén en dos o más cursos.")
        return

    for legajo in alumnosConocidos:
        alumno = busqueda.buscarAlumnoPorLegajo(legajo)
        if alumno:
            cursosAlumno = [idC for (idC, _) in alumno["cursos"] if any(c["id"] == idC for c in cursosProfesor)]
            cursosStr = ", ".join(cursosAlumno)
            print(headers.Fore.WHITE + f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']} | Cursos: {cursosStr}")