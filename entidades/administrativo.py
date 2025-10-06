import entidades.datos as datos # Importamos la base de datos centralizada

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
    for credencial in datos.CREDENCIALES:
        print("----------------------------------")
        print(f"Legajo: {credencial['legajo']}")
        print(f"Clave: {credencial['clave']}")
        print(f"Rol: {credencial['rol']}")
        print("----------------------------------")

"""
La funcion pide: Nombre, Apellido
- añade un alumno a la lista
- muestra un resumen del alumno al finalizar
"""
def registrarAlumno():
    """
    estructura de Alumno:
    Legajo, Nombre, Apellido, Cursos = [], Pagos_pendientes = []
    """
    legajo = max([al["legajo"] for al in datos.ALUMNOS_DB], default=100) + 1
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
        "cursos": [],  # lista de tuplas (idCurso, estado)
        "pagos_pendientes": []
    }
    # guardamos credenciales
    alumnoCredenciales = {
        "legajo": legajo,
        "clave": clave,
        "rol" : "alumno"
    }
    # insertamos los datos
    datos.ALUMNOS_DB.append(nuevoAlumno)
    datos.CREDENCIALES.append(alumnoCredenciales)
    # mostramos resumen
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
    legajo = max([prof["legajo"] for prof in datos.PROFESORES_DB], default=2000) + 1
    print(f"Legajo: {legajo}")
    nombre = input("Ingrese nombre del profesor: ")
    apellido = input("Ingrese apellido del profesor: ")
    # creamos una clave generica
    clave = str(nombre) + str(legajo)
    # estructura del profesor para la lista principal
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
    datos.PROFESORES_DB.append(nuevoProfesor)
    datos.CREDENCIALES.append(profesorCredenciales)
    # mostramos resumen
    print("¡Profesor generado existosamente!")
    print("-------------------------------")
    print(f"Profesor: {apellido}, {nombre}")
    print(f"Legajo: {legajo}")
    print(f"Clave: {clave}")
    print("-------------------------------")

"""
La funcion pide legajo del profesor y materia
- consulta si ese profesor ya fue asignado a esa materia
- asigna el profesor a la materia
"""
def asignarCursoAProfesor(legajoProf):
    ###### PROFESOR
    # chequeamos que haya profesores y si existe
    profesorEncontrado = next((p for p in datos.PROFESORES_DB if p["legajo"] == legajoProf), None)
    if not profesorEncontrado:
        print("Profesor no encontrado.")
        return
    ####### CURSO
    # chequeamos que haya cursos
    if datos.CURSOS_DB:
        print("\n--- Cursos disponibles ---")
        for curso in datos.CURSOS_DB:
            prof = next((p for p in datos.PROFESORES_DB if p["legajo"] == curso["profesor"]), None)
            nombre_prof = f"{prof['nombre']} {prof['apellido']}" if prof else "Sin asignar"
            print(f"{curso['id']} - {curso['nombre']} (Profesor: {nombre_prof})")
        # Pedimos curso
        idCurso = input("Ingrese el ID del curso a asignar: ")
        # Buscamos el curso
        cursoEncontrado = next((c for c in datos.CURSOS_DB if c["id"] == idCurso), None)
        if not cursoEncontrado:
            print("Curso no encontrado.")
            return
        cursoEncontrado["profesor"] = profesorEncontrado["legajo"]
        # hacemos una validacion para no agregar dos veces el mismo
        if cursoEncontrado["id"] not in profesorEncontrado["materias"]:
            profesorEncontrado["materias"].append(cursoEncontrado["id"])
        print(f"Curso {cursoEncontrado['nombre']} asignado al profesor {profesorEncontrado['nombre']}.")
    # si no hay cursos
    else:
        print("No hay cursos disponibles. Por favor ingresar un curso primero.")
        return

def aprobarPago():
    """Aprueba el pago de un alumno (mueve de pendientes a pagadas)."""
    print("\n--- APROBAR PAGO ---")
    legajo = int(input("Ingrese el legajo del alumno: "))
    cuotas = [c for c in datos.CUOTAS_PENDIENTES if c["legajo"] == legajo]

    if not cuotas:
        print("El alumno no tiene pagos pendientes.")
        return

    print("Pagos pendientes:")
    for cuota in cuotas:
        print(f"Cuota N°{cuota['cuota_nro']}")

    nro = int(input("Ingrese el número de cuota a aprobar: "))
    cuota = next((c for c in cuotas if c["cuota_nro"] == nro), None)

    if cuota:
        datos.CUOTAS_PENDIENTES.remove(cuota)
        print(f"Pago de cuota N°{nro} aprobado para el alumno {legajo}.")
    else:
        print("Número de cuota inválido.")

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
            legajo = int(input("Ingrese el legajo del profesor: "))
            asignarCursoAProfesor(legajo)
        elif opcion == 4:
            aprobarPago()
        else:
            print("Opción no válida. Intente de nuevo.")
        menuOpciones()
        opcion = int(input("Seleccione una opción: "))
    print("Volviendo al menú principal...")

if __name__ == "__main__":
    menuAdministrativo()