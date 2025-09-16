import datos  # Importamos la base de datos centralizada

def registrarAlumno():
    """Da de alta un nuevo alumno."""
    legajo = int(input("Ingrese legajo del alumno: "))
    nombre = input("Ingrese nombre del alumno: ")

    for alumno in datos.ALUMNOS_DB:
        if alumno["legajo"] == legajo:
            print(f"Error: El legajo {legajo} ya está registrado.")
            return

    nuevoAlumno = {
        "legajo": legajo,
        "nombre": nombre,
        "cursosInscriptos": [],
        "pagosAdeudados": False,
        "estadoAprobacion": "Desaprobado",
    }
    datos.ALUMNOS_DB.append(nuevoAlumno)
    print(f"Alumno {nombre} registrado con éxito.")


def registrarProfesor():
    """Da de alta un nuevo profesor."""
    legajo = int(input("Ingrese legajo del profesor: "))
    nombre = input("Ingrese nombre del profesor: ")

    for profesor in datos.PROFESORES_DB:
        if profesor["legajo"] == legajo:
            print(f"Error: El legajo {legajo} ya está registrado.")
            return

    nuevoProfesor = {
        "legajo": legajo,
        "nombre": nombre,
        "materias": []
    }
    datos.PROFESORES_DB.append(nuevoProfesor)
    print(f"Profesor {nombre} registrado con éxito.")


def asignarCursoAProfesor():
    """Asigna un curso a un profesor."""
    legajoProf = int(input("Ingrese legajo del profesor: "))
    profesor = None
    for p in datos.PROFESORES_DB:
        if p["legajo"] == legajoProf:
            profesor = p
            break
    if not profesor:
        print("Profesor no encontrado.")
        return

    print("\n--- Cursos disponibles ---")
    for curso in datos.CURSOS_DB:
        print(f"{curso['id']} - {curso['nombre']} (Profesor: {curso['profesor']})")

    idCurso = input("Ingrese el ID del curso a asignar: ")
    curso = None
    for c in datos.CURSOS_DB:
        if c["id"] == idCurso:
            curso = c
            break
    if not curso:
        print("Curso no encontrado.")
        return

    curso["profesor"] = profesor["nombre"]
    profesor["materias"].append(curso["id"])
    print(f"Curso {curso['nombre']} asignado al profesor {profesor['nombre']}.")


def aprobarPago():
    """Aprueba el pago de un alumno (mueve de pendientes a pagadas)."""
    legajo = int(input("Ingrese legajo del alumno: "))
    cuotaNro = int(input("Ingrese número de cuota a aprobar: "))

    for cuota in datos.CUOTAS_PENDIENTES:
        if cuota["legajo"] == legajo and cuota["cuota_nro"] == cuotaNro:
            datos.CUOTAS_PENDIENTES.remove(cuota)
            print(f"Cuota {cuotaNro} del alumno {legajo} aprobada.")
            return
    print("No se encontró esa cuota pendiente.")


def menuOpciones():
    print("\n--- MENÚ ADMINISTRATIVO ---")
    print("1. Registrar alumno")
    print("2. Registrar profesor")
    print("3. Asignar curso a profesor")
    print("4. Aprobar pago de alumno")
    print("5. Volver al menú principal")


def menuAdministrativo():
    """Muestra el menú de opciones para un Administrativo."""
    menuOpciones()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 5:
        if opcion == 1:
            registrarAlumno()
        elif opcion == 2:
            registrarProfesor()
        elif opcion == 3:
            asignarCursoAProfesor()
        elif opcion == 4:
            aprobarPago()
        else:
            print("Opción no válida. Intente de nuevo.")

        menuOpciones()
        opcion = int(input("Seleccione una opción: "))

    print("Volviendo al menú principal...")