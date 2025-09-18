from entidades.datos import PROFESORES_DB, ALUMNOS_DB, CREDENCIALES # Importamos la base de datos centralizada

"""
### Funcionalidades que debe hacer el administrativo:
1. Dar de alta alumnos
2. Dar de alta profesores
3. Dar de alta materias
4. Asignar un profesor a una materia
5. Aprobar un pago pendiente de un Alumno
### Restricciones
3. No se puede crear 2 materias con el mismo nombre
"""

############ FUNCIONES ###############
"""
La funcion no recibe parametros
- muestra listado de Credenciales existentes
"""
def verCredenciales():
    for credencial in CREDENCIALES:
        print("----------------------------------")
        print(f"Legajo: {credencial["legajo"]}")
        print(f"Clave: {credencial["clave"]}")
        print(f"Rol: {credencial["rol"]}")
        print("----------------------------------")

"""
La funcion pide: Nombre, Apellido
- añade un alumno a la lista
- muestra un resumen del alumno al finalizar
"""
def registrarAlumno():
    """
    estructura de Alumno:
    Legajo, Nombre, Apellido, Materias = [], Pagos_pendientes = []
    """
    legajo = 1
    if len(ALUMNOS_DB) != 0:
        legajo = len(ALUMNOS_DB) + 1
    print(f"Legajo: {legajo}")
    nombre = input("Ingrese nombre del alumno: ")
    apellido = input("Ingrese apellido del alumno: ")
    # creamos una clave generica
    clave = str(nombre) + str(legajo)
    # estructura del alumno para la lista principal
    nuevoAlumno = {
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido,
        "materias": [],
        "pagos_pendientes": [],
    }
    # guardamos credenciales
    alumnoCredenciales = {
        "legajo": legajo,
        "clave": clave,
        "rol" : "alumno"
    }
    # insertamos los datos
    ALUMNOS_DB.append(nuevoAlumno)
    CREDENCIALES.append(alumnoCredenciales)
    print("¡Alumno generado existosamente!")
    print("-------------------------------")
    print(f"Alumno: {apellido}, {nombre}")
    print(f"Legajo: {legajo}")
    print(f"Clave: {clave}")
    print("-------------------------------")

"""
La funcion pide: Nombre, Apellido
- añade un profesor a la lista
- muestra un resumen del profesor al finalizar
"""
def registrarProfesor():
    """
    estructura de Profesor:
    Legajo, Nombre, Apellido, Materias = []
    """
    legajo = 1
    if len(PROFESORES_DB) != 0:
        legajo = len(PROFESORES_DB) + 1
    print(f"Legajo: {legajo}")
    nombre = input("Ingrese nombre del profesor: ")
    apellido = input("Ingrese apellido del profesor: ")
    # creamos una clave generica
    clave = str(nombre) + str(legajo)
    # estructura del alumno para la lista principal
    nuevoProfesor = {
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido,
        "materias": []
    }
    # guardamos credenciales
    profesorCredenciales = {
        "legajo": legajo,
        "clave": clave,
        "rol" : "profesor"
    }
    # insertamos los datos
    PROFESORES_DB.append(nuevoProfesor)
    CREDENCIALES.append(profesorCredenciales)
    print("¡Profesor generado existosamente!")
    print("-------------------------------")
    print(f"Profesor: {apellido}, {nombre}")
    print(f"Legajo: {legajo}")
    print(f"Clave: {clave}")
    print("-------------------------------")


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
    print("--- MENÚ ADMINISTRATIVO ---")
    print("0. Ver credenciales existentes")
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
        if opcion == 0:
            verCredenciales()
        elif opcion == 1:
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

if __name__ == "__main__":
    menuAdministrativo()