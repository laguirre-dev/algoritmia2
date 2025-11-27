from . import datos_backup2 as datos_backup2
from utils import pantalla as headers
from utils import busquedas as busqueda


def aprobarODesaprobarAlumnos(legajoProfesor):
    cursosProfesor = list(
        filter(lambda c: c.get("profesor") == legajoProfesor, datos_backup2.CURSOS_DB)
    )
    if not cursosProfesor:
        print(headers.Fore.RED + "No tenés cursos asignados.")
        return

    headers.header("MIS CURSOS")
    for curso in cursosProfesor:
        print(
            headers.Fore.WHITE
            + f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']}"
        )

    idCurso = input(
        headers.Fore.WHITE + "\nIngrese el ID del curso que desea gestionar: "
    )
    curso = busqueda.buscarCursoPorId(idCurso)

    if not curso or curso.get("profesor") != legajoProfesor:
        print(headers.Fore.RED + "Curso no válido o no pertenece a este profesor.")
        return

    if not curso.get("alumnos"):
        print(headers.Fore.RED + "No hay alumnos inscriptos en este curso.")
        return

    headers.header(f"ALUMNOS EN {curso['nombre']}")
    for legajo in curso["alumnos"]:
        alumno = busqueda.buscarAlumnoPorLegajo(legajo)
        if alumno:
            estado = next(
                (estado for (idC, estado) in alumno["cursos"] if idC == idCurso),
                "Desaprobado",
            )
            colorEstado = (
                headers.Fore.GREEN if estado == "Aprobado" else headers.Fore.RED
            )
            print(
                headers.Fore.WHITE
                + f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']} | Estado: "
                + colorEstado
                + estado
            )

    entrada = input(
        headers.Fore.WHITE
        + "\nIngrese legajo y acción (A=aprobar, D=desaprobar) separados por coma. Ej: 101:A, 102:D\n> "
    )
    acciones = list(
        map(
            lambda x: (int(x.split(":")[0].strip()), x.split(":")[1].strip().upper()),
            filter(lambda y: ":" in y, entrada.split(",")),
        )
    )

    for legajo, accion in acciones:
        alumno = busqueda.buscarAlumnoPorLegajo(legajo)
        if alumno and legajo in curso["alumnos"]:
            for i, (idC, estado) in enumerate(alumno["cursos"]):
                if idC == idCurso:
                    if accion == "A":
                        alumno["cursos"][i] = (idC, "Aprobado")
                        print(
                            headers.Fore.GREEN
                            + f"Alumno {alumno['nombre']} {alumno['apellido']} aprobado en {idCurso}."
                        )
                    elif accion == "D":
                        alumno["cursos"][i] = (idC, "Desaprobado")
                        print(
                            headers.Fore.RED
                            + f"Alumno {alumno['nombre']} {alumno['apellido']} desaprobado en {idCurso}."
                        )


def aprobarODesaprobarAlumnosMock(legajoProfesor, idCurso, entrada):
    cursosProfesor = list(
        filter(lambda c: c.get("profesor") == legajoProfesor, datos_backup2.CURSOS_DB)
    )
    if not cursosProfesor:
        print(headers.Fore.RED + "No tenés cursos asignados.")
        return

    headers.header("MIS CURSOS")
    for curso in cursosProfesor:
        print(
            headers.Fore.WHITE
            + f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']}"
        )

    # idCurso = input(headers.Fore.WHITE + "\nIngrese el ID del curso que desea gestionar: ")
    curso = busqueda.buscarCursoPorId(idCurso)

    if not curso or curso.get("profesor") != legajoProfesor:
        print(headers.Fore.RED + "Curso no válido o no pertenece a este profesor.")
        return

    if not curso.get("alumnos"):
        print(headers.Fore.RED + "No hay alumnos inscriptos en este curso.")
        return

    headers.header(f"ALUMNOS EN {curso['nombre']}")
    for legajo in curso["alumnos"]:
        alumno = busqueda.buscarAlumnoPorLegajo(legajo)
        if alumno:
            estado = next(
                (estado for (idC, estado) in alumno["cursos"] if idC == idCurso),
                "Desaprobado",
            )
            colorEstado = (
                headers.Fore.GREEN if estado == "Aprobado" else headers.Fore.RED
            )
            print(
                headers.Fore.WHITE
                + f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']} | Estado: "
                + colorEstado
                + estado
            )

    # entrada = input(headers.Fore.WHITE + "\nIngrese legajo y acción (A=aprobar, D=desaprobar) separados por coma. Ej: 101:A, 102:D\n> ")
    acciones = list(
        map(
            lambda x: (int(x.split(":")[0].strip()), x.split(":")[1].strip().upper()),
            filter(lambda y: ":" in y, entrada.split(",")),
        )
    )

    for legajo, accion in acciones:
        alumno = busqueda.buscarAlumnoPorLegajo(legajo)
        if alumno and legajo in curso["alumnos"]:
            for i, (idC, estado) in enumerate(alumno["cursos"]):
                if idC == idCurso:
                    if accion == "A":
                        alumno["cursos"][i] = (idC, "Aprobado")
                        print(
                            headers.Fore.GREEN
                            + f"Alumno {alumno['nombre']} {alumno['apellido']} aprobado en {idCurso}."
                        )
                        return ["Aprobado", alumno["legajo"]]
                    elif accion == "D":
                        alumno["cursos"][i] = (idC, "Desaprobado")
                        print(
                            headers.Fore.RED
                            + f"Alumno {alumno['nombre']} {alumno['apellido']} desaprobado en {idCurso}."
                        )
                        return ["Desaprobado", alumno["legajo"]]
