import entidades.datos as datos
from colorama import init, Fore, Style

# Inicializamos colorama
init(autoreset=True)

def header(titulo):
    # Encabezado estilizado con onda universitaria
    print(Fore.GREEN + "=" * 50)
    print(Style.BRIGHT + Fore.WHITE + titulo.center(50))
    print(Fore.GREEN + "=" * 50)

def verMisCursos(legajoProfesor):
    cursosProfesor = list(filter(lambda c: c.get("profesor") == legajoProfesor, datos.CURSOS_DB))
    if not cursosProfesor:
        print(Fore.RED + "No tenés cursos asignados.")
        return
    header("MIS CURSOS")
    for curso in cursosProfesor:
        print(Fore.WHITE + f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']}")

def verMisAlumnos(legajoProfesor):
    cursosProfesor = list(filter(lambda c: c.get("profesor") == legajoProfesor, datos.CURSOS_DB))
    if not cursosProfesor:
        print(Fore.RED + "No tenés cursos asignados.")
        return

    header("MIS ALUMNOS")

    # Conjunto con todos los alumnos únicos de los cursos del profesor
    alumnosSet = set()
    for curso in cursosProfesor:
        alumnosSet.update(curso.get("alumnos", []))

    if not alumnosSet:
        print(Fore.RED + "No hay alumnos inscriptos en tus cursos.")
        return

    for legajo in alumnosSet:
        alumno = buscarAlumnoPorLegajo(legajo)
        if alumno:
            estados = [(idC, estado) for (idC, estado) in alumno["cursos"] if any(c["id"] == idC for c in cursosProfesor)]
            estadosStr = ", ".join([f"{idC}: {estado}" for idC, estado in estados])
            print(Fore.WHITE + f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']} | Cursos: {estadosStr}")

def alumnoConocido(legajoProfesor):
    cursosProfesor = [c for c in datos.CURSOS_DB if c.get("profesor") == legajoProfesor]
    if not cursosProfesor:
        print(Fore.RED + "No tenés cursos asignados.")
        return

    conjuntosAlumnos = [set(curso.get("alumnos", [])) for curso in cursosProfesor if curso.get("alumnos")]

    if len(conjuntosAlumnos) < 2:
        print(Fore.RED + "No hay alumnos que estén en dos o más cursos.")
        return

    alumnosConocidos = set()
    for i in range(len(conjuntosAlumnos)):
        for j in range(i + 1, len(conjuntosAlumnos)):
            alumnosConocidos |= (conjuntosAlumnos[i] & conjuntosAlumnos[j])

    header("ALUMNOS CONOCIDOS")
    if not alumnosConocidos:
        print(Fore.RED + "No hay alumnos que estén en dos o más cursos.")
        return

    for legajo in alumnosConocidos:
        alumno = buscarAlumnoPorLegajo(legajo)
        if alumno:
            cursosAlumno = [idC for (idC, _) in alumno["cursos"] if any(c["id"] == idC for c in cursosProfesor)]
            cursosStr = ", ".join(cursosAlumno)
            print(Fore.WHITE + f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']} | Cursos: {cursosStr}")
            
def aprobarODesaprobarAlumnos(legajoProfesor):
    cursosProfesor = list(filter(lambda c: c.get("profesor") == legajoProfesor, datos.CURSOS_DB))
    if not cursosProfesor:
        print(Fore.RED + "No tenés cursos asignados.")
        return

    header("MIS CURSOS")
    for curso in cursosProfesor:
        print(Fore.WHITE + f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']}")

    idCurso = input(Fore.WHITE + "\nIngrese el ID del curso que desea gestionar: ")
    curso = buscarCursoPorId(idCurso)

    if not curso or curso.get("profesor") != legajoProfesor:
        print(Fore.RED + "Curso no válido o no pertenece a este profesor.")
        return

    if not curso.get("alumnos"):
        print(Fore.RED + "No hay alumnos inscriptos en este curso.")
        return

    header(f"ALUMNOS EN {curso['nombre']}")
    for legajo in curso["alumnos"]:
        alumno = buscarAlumnoPorLegajo(legajo)
        if alumno:
            estado = next((estado for (idC, estado) in alumno["cursos"] if idC == idCurso), "Desaprobado")
            colorEstado = Fore.GREEN if estado == "Aprobado" else Fore.RED
            print(Fore.WHITE + f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']} | Estado: " + colorEstado + estado)

    entrada = input(Fore.WHITE + "\nIngrese legajo y acción (A=aprobar, D=desaprobar) separados por coma. Ej: 101:A, 102:D\n> ")
    acciones = list(
        map(
            lambda x: (int(x.split(":")[0].strip()), x.split(":")[1].strip().upper()),
            filter(lambda y: ":" in y, entrada.split(","))
        )
    )

    for legajo, accion in acciones:
        alumno = buscarAlumnoPorLegajo(legajo)
        if alumno and legajo in curso["alumnos"]:
            for i, (idC, estado) in enumerate(alumno["cursos"]):
                if idC == idCurso:
                    if accion == "A":
                        alumno["cursos"][i] = (idC, "Aprobado")
                        print(Fore.GREEN + f"Alumno {alumno['nombre']} {alumno['apellido']} aprobado en {idCurso}.")
                    elif accion == "D":
                        alumno["cursos"][i] = (idC, "Desaprobado")
                        print(Fore.RED + f"Alumno {alumno['nombre']} {alumno['apellido']} desaprobado en {idCurso}.")

def verAlumnosDeCurso():
    idCurso = input(Fore.WHITE + "Ingrese el ID del curso: ")
    curso = buscarCursoPorId(idCurso)
    if not curso:
        print(Fore.RED + "Curso no encontrado.")
        return

    if not curso.get("alumnos"):
        print(Fore.RED + "No hay alumnos inscriptos en este curso.")
        return

    header(f"ALUMNOS DEL CURSO {curso['nombre']}")
    for legajo in set(curso["alumnos"]):  
        alumno = buscarAlumnoPorLegajo(legajo)
        if alumno:
            print(Fore.WHITE + f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']}")
        else:
            print(Fore.RED + f"Legajo {legajo} no encontrado en la base de datos.")

def menuOpciones():
    header("MENÚ PROFESOR")
    print(Fore.GREEN + "1. Visualizar cursos y aulas")
    print(Fore.GREEN + "2. Aprobar o desaprobar alumnos")
    print(Fore.GREEN + "3. Generar reporte de alumnos -- En desarrollo")
    print(Fore.GREEN + "4. Mis gestiones -- En desarrollo")
    print(Fore.RED   + "5. Volver al menú principal")

def menuVisualizar():
    header("MENÚ PROFESOR - ALUMNOS Y CURSOS")
    print(Fore.GREEN + "1. Mis cursos")
    print(Fore.GREEN + "2. Mis alumnos")
    print(Fore.GREEN + "3. Alumno Conocido")
    print(Fore.RED   + "4. Volver al menú profesor")

def menuProfesor(legajoProfesor):
    menuOpciones()
    opcion = int(input(Fore.WHITE + "Seleccione una opción: "))
    while opcion != 5:
        if opcion == 1:
            menuVisualizar()
            subopcion = int(input(Fore.WHITE + "Seleccione una opción: "))
            while subopcion != 4:
                if subopcion == 1:
                    verMisCursos(legajoProfesor)
                elif subopcion == 2:
                    verMisAlumnos(legajoProfesor)
                elif subopcion == 3:
                    alumnoConocido(legajoProfesor)
                else:
                    print(Fore.RED + "Opción no válida. Intente de nuevo.")
                menuVisualizar()
                subopcion = int(input(Fore.WHITE + "Seleccione una opción: "))
        elif opcion == 2:
            aprobarODesaprobarAlumnos(legajoProfesor)
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")
        menuOpciones()
        opcion = int(input(Fore.WHITE + "Seleccione una opción: "))
    print(Fore.RED + "Volviendo al menú principal...")

def buscarCursoPorId(idCurso):
    return next((curso for curso in datos.CURSOS_DB if curso.get("id") == idCurso), None)

def buscarAlumnoPorLegajo(legajo):
    return next((alumno for alumno in datos.ALUMNOS_DB if alumno.get("legajo") == legajo), None)

if __name__ == "__main__":
    menuProfesor()