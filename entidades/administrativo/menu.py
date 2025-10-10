"""
Meter solo el acceso a los modulos desde aca

Cambios hacer en el administrativo
Agregar funciones lambda
Agregar listas por comprension
Agregar filter, map y metodos de listas


Funcionalidades que debe hacer el administrativo:
1. Altas y bajas de alumnos, profesores, carreras y materias
2. Asigna profesores a las materias
3. Aprueba pagos de alumnos

Para organizarlo un poco mejor, vamos a separar esto en 3 submenus: Gestion de usuarios, Gestion de materias, Gestion de pagos
"""


import entidades.datos as datos  # Importamos la base de datos centralizada
from colorama import init, Fore, Style

# Inicializamos colorama
init(autoreset=True)

"""
### Funcionalidades que debe hacer el administrativo:
1. Dar de alta alumnos - gestion usuarios
2. Dar de alta profesores - gestion usuarios
3. Dar de alta materias - gestion materias
4. Asignar un profesor a una materia - gestion materias
5. Aprobar un pago a un Alumno - gestion pagos
### Restricciones
3. No se puede crear 2 materias con el mismo nombre
"""

def header(titulo):
    # Encabezado estilizado con onda universitaria
    print(Fore.GREEN + "=" * 50)
    print(Style.BRIGHT + Fore.WHITE + titulo.center(50))
    print(Fore.GREEN + "=" * 50)

############ FUNCIONES ###############
"""
La funcion no recibe parametros
- muestra listado de Credenciales existentes
"""
def verCredenciales():
    header("CREDENCIALES EXISTENTES")
    for credencial in datos.CREDENCIALES:
        print(Fore.WHITE + "----------------------------------")
        print(Fore.WHITE + f"Legajo: {credencial['legajo']}")
        print(Fore.WHITE + f"Clave: {credencial['clave']}")
        print(Fore.WHITE + f"Rol: {credencial['rol']}")
        print(Fore.WHITE + "----------------------------------")

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
    print(Fore.WHITE + f"Legajo: {legajo}")
    nombre = input(Fore.WHITE + "Ingrese nombre del alumno: ")
    apellido = input(Fore.WHITE + "Ingrese apellido del alumno: ")
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
        "rol": "alumno"
    }
    # insertamos los datos
    datos.ALUMNOS_DB.append(nuevoAlumno)
    datos.CREDENCIALES.append(alumnoCredenciales)
    # mostramos resumen
    header("ALUMNO REGISTRADO")
    print(Fore.WHITE + f"Alumno: {apellido}, {nombre}")
    print(Fore.WHITE + f"Legajo: {legajo}")
    print(Fore.WHITE + f"Clave: {clave}")

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
    print(Fore.WHITE + f"Legajo: {legajo}")
    nombre = input(Fore.WHITE + "Ingrese nombre del profesor: ")
    apellido = input(Fore.WHITE + "Ingrese apellido del profesor: ")
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
        "rol": "profesor"
    }
    # insertamos los datos
    datos.PROFESORES_DB.append(nuevoProfesor)
    datos.CREDENCIALES.append(profesorCredenciales)
    # mostramos resumen
    header("PROFESOR REGISTRADO")
    print(Fore.WHITE + f"Profesor: {apellido}, {nombre}")
    print(Fore.WHITE + f"Legajo: {legajo}")
    print(Fore.WHITE + f"Clave: {clave}")

"""
La funcion pide legajo del profesor y materia
- consulta si ese profesor ya fue asignado a esa materia
- asigna el profesor a la materia
"""
def asignarCursoAProfesor(legajoProf):
    ###### PROFESOR
    profesorEncontrado = next((p for p in datos.PROFESORES_DB if p["legajo"] == legajoProf), None)
    if not profesorEncontrado:
        print(Fore.RED + "Profesor no encontrado.")
        return
    ####### CURSO
    if datos.CURSOS_DB:
        header("CURSOS DISPONIBLES")
        for curso in datos.CURSOS_DB:
            prof = next((p for p in datos.PROFESORES_DB if p["legajo"] == curso["profesor"]), None)
            nombreProf = f"{prof['nombre']} {prof['apellido']}" if prof else "Sin asignar"
            print(Fore.WHITE + f"{curso['id']} - {curso['nombre']} (Profesor: {nombreProf})")
        idCurso = input(Fore.WHITE + "Ingrese el ID del curso a asignar: ")
        cursoEncontrado = next((c for c in datos.CURSOS_DB if c["id"] == idCurso), None)
        if not cursoEncontrado:
            print(Fore.RED + "Curso no encontrado.")
            return
        cursoEncontrado["profesor"] = profesorEncontrado["legajo"]
        if cursoEncontrado["id"] not in profesorEncontrado["materias"]:
            profesorEncontrado["materias"].append(cursoEncontrado["id"])
        print(Fore.GREEN + f"Curso {cursoEncontrado['nombre']} asignado al profesor {profesorEncontrado['nombre']}.")
    else:
        print(Fore.RED + "No hay cursos disponibles. Por favor ingresar un curso primero.")
        return

def aprobarPago():
    """Aprueba el pago de un alumno (mueve de pendientes a pagadas)."""
    header("APROBAR PAGO")
    legajo = int(input(Fore.WHITE + "Ingrese el legajo del alumno: "))
    cuotas = [c for c in datos.CUOTAS_PENDIENTES if c["legajo"] == legajo]

    if not cuotas:
        print(Fore.RED + "El alumno no tiene pagos pendientes.")
        return

    print(Fore.WHITE + "Pagos pendientes:")
    for cuota in cuotas:
        print(Fore.WHITE + f"Cuota N°{cuota['cuota_nro']}")

    nro = int(input(Fore.WHITE + "Ingrese el número de cuota a aprobar: "))
    cuota = next((c for c in cuotas if c["cuota_nro"] == nro), None)

    if cuota:
        datos.CUOTAS_PENDIENTES.remove(cuota)
        print(Fore.GREEN + f"Pago de cuota N°{nro} aprobado para el alumno {legajo}.")
    else:
        print(Fore.RED + "Número de cuota inválido.")

def menuOpciones():
    header("MENÚ ADMINISTRATIVO")
    print(Fore.GREEN + "0. Ver credenciales existentes")
    print(Fore.GREEN + "1. Registrar alumno")
    print(Fore.GREEN + "2. Registrar profesor")
    print(Fore.GREEN + "3. Asignar curso a profesor")
    print(Fore.GREEN + "4. Aprobar pago de alumno")
    print(Fore.RED   + "5. Volver al menú principal")

def menuAdministrativo():
    """Muestra el menú de opciones para un Administrativo."""
    menuOpciones()
    opcion = int(input(Fore.WHITE + "Seleccione una opción: "))
    while opcion != 5:
        if opcion == 0:
            verCredenciales()
        elif opcion == 1:
            registrarAlumno()
        elif opcion == 2:
            registrarProfesor()
        elif opcion == 3:
            legajo = int(input(Fore.WHITE + "Ingrese el legajo del profesor: "))
            asignarCursoAProfesor(legajo)
        elif opcion == 4:
            aprobarPago()
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")
        menuOpciones()
        opcion = int(input(Fore.WHITE + "Seleccione una opción: "))
    print(Fore.RED + "Volviendo al menú principal...")

if __name__ == "__main__":
    menuAdministrativo()