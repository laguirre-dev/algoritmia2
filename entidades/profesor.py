import entidades.datos as datos  # profesor.py

def verMisCursos(legajoProfesor):
    cursosProfesor = list(filter(lambda c: c.get("profesor") == legajoProfesor, datos.CURSOS_DB))
    if not cursosProfesor:
        print("No tenés cursos asignados.")
        return
    print("\n--- MIS CURSOS ---")
    cursos_str = map(lambda c: f"{c['id']} - {c['nombre']} | Aula: {c['aula']}", cursosProfesor)
    print("\n".join(cursos_str))


def verMisAlumnos(legajoProfesor):
    cursosProfesor = list(filter(lambda c: c.get("profesor") == legajoProfesor, datos.CURSOS_DB))
    if not cursosProfesor:
        print("No tenés cursos asignados.")
        return
    print("\n--- MIS ALUMNOS ---")
    for curso in cursosProfesor:
        print(f"\nCurso: {curso['id']} - {curso['nombre']}")
        if not curso.get("alumnos"):
            print("  No hay alumnos inscriptos.")
        else:
            for legajo in curso["alumnos"]:
                alumno = buscarAlumnoPorLegajo(legajo)
                if alumno:
                    estado = next((estado for (idC, estado) in alumno["cursos"] if idC == curso["id"]), "Desaprobado")
                    print(f"  {alumno['legajo']} - {alumno['nombre']} {alumno['apellido']} | Estado: {estado}")


def aprobarODesaprobarAlumnos(legajoProfesor):
    cursosProfesor = list(filter(lambda c: c.get("profesor") == legajoProfesor, datos.CURSOS_DB))
    if not cursosProfesor:
        print("No tenés cursos asignados.")
        return

    print("\n--- MIS CURSOS ---")
    for curso in cursosProfesor:
        print(f"{curso['id']} - {curso['nombre']} | Aula: {curso['aula']}")

    idCurso = input("\nIngrese el ID del curso que desea gestionar: ")
    curso = buscarCursoPorId(idCurso)

    if not curso or curso.get("profesor") != legajoProfesor:
        print("Curso no válido o no pertenece a este profesor.")
        return

    if not curso.get("alumnos"):
        print("No hay alumnos inscriptos en este curso.")
        return

    print(f"\n--- Alumnos en {curso['nombre']} ---")
    for legajo in curso["alumnos"]:
        alumno = buscarAlumnoPorLegajo(legajo)
        if alumno:
            estado = next((estado for (idC, estado) in alumno["cursos"] if idC == idCurso), "Desaprobado")
            print(f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']} | Estado: {estado}")

    entrada = input("\nIngrese legajo y acción (A=aprobar, D=desaprobar) separados por coma. Ej: 101:A, 102:D\n> ")
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
                        print(f"Alumno {alumno['nombre']} {alumno['apellido']} aprobado en {idCurso}.")
                    elif accion == "D":
                        alumno["cursos"][i] = (idC, "Desaprobado")
                        print(f"Alumno {alumno['nombre']} {alumno['apellido']} desaprobado en {idCurso}.")


def verAlumnosDeCurso():
    idCurso = input("Ingrese el ID del curso: ")
    curso = buscarCursoPorId(idCurso)
    if not curso:
        print("Curso no encontrado.")
        return

    if not curso.get("alumnos"):
        print("No hay alumnos inscriptos en este curso.")
        return

    print(f"\n--- Alumnos del curso {curso['nombre']} ---")
    for legajo in curso["alumnos"]:
        alumno = buscarAlumnoPorLegajo(legajo)
        if alumno:
            print(f"{alumno['legajo']} - {alumno['nombre']} {alumno['apellido']}")
        else:
            print(f"Legajo {legajo} no encontrado en la base de datos.")


def menuOpciones():
    print("\n--- MENÚ PROFESOR ---")
    print("1. Visualizar cursos y aulas")
    print("2. Aprobar o desaprobar alumnos")
    print("3. Generar reporte de alumnos -- En desarrollo")
    print("4. Mis gestiones -- En desarrollo")
    print("5. Volver al menú principal")


def menuVisualizar():
    print("\n--- MENÚ VISUALIZAR ---")
    print("1. Mis cursos")
    print("2. Mis alumnos")
    print("3. Volver al menú profesor")


def menuProfesor(legajoProfesor):
    menuOpciones()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 5: 
        if opcion == 1:
            menuVisualizar()
            subopcion = int(input("Seleccione una opción: "))
            while subopcion != 3:
                if subopcion == 1:
                    verMisCursos(legajoProfesor)
                elif subopcion == 2:
                    verMisAlumnos(legajoProfesor)
                else:
                    print("Opción no válida. Intente de nuevo.")
                menuVisualizar()
                subopcion = int(input("Seleccione una opción: "))
        elif opcion == 2:
            aprobarODesaprobarAlumnos(legajoProfesor)
        else:
            print("Opción no válida. Intente de nuevo.")
        menuOpciones()
        opcion = int(input("Seleccione una opción: "))
    print("Volviendo al menú principal...")


def buscarCursoPorId(idCurso):
    return next((curso for curso in datos.CURSOS_DB if curso.get("id") == idCurso), None)


def buscarAlumnoPorLegajo(legajo):
    return next((alumno for alumno in datos.ALUMNOS_DB if alumno.get("legajo") == legajo), None)


if __name__ == "__main__":
    menuProfesor()