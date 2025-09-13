# profesor.py
def menu_opciones():
    print("\n--- MENÚ PROFESOR ---")
    print("1. Visualizar cursos y aulas")
    print("2. Aprobar o desaprobar alumnos")
    print("3. Volver al menú principal")


def menu_profesor():
    """Muestra el menú de opciones para un Profesor."""
    menu_opciones()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 3:
        if opcion == 1:
            print("Visualizar cursos y aulas - Funcionalidad en desarrollo.")
        elif opcion == 2:
            print("Aprobar o desaprobar alumnos - Funcionalidad en desarrollo.")
        else:
            print("Opción no válida. Intente de nuevo.")
        menu_opciones()
        opcion = int(input("Seleccione una opción: "))
    print("Volviendo al menú principal...")


# Diccionario de Facultad y que se pueda dar de alta Facultades
UADE = []
UADE = [
    {
        "Nombre": "FAIC",
        "Materias" : []
    },
    {
        "Nombre": "FAIN",
        "Materias" : []
    },
    {
        "Nombre": "FADU",
        "Materias" : []
    },
]
# Login diccionario
Credeciales = [
    {
        "User" : "",
        "Password" : "",
        "Rol": ""
    },
]
# Datos para Alumno
Alumno = {
    "Legajo" : 0,
    "Nombres" : "",
    "Apellido" : "",
    "Cuotas_pendientes" : [],
    "Materias" : [],
}
# Datos para Materia
Materia = [
    {
        "Nombre" :"",
        "Aula": "",
        "Profesor_asignado":"", #legajo_profesor
        "Alumnos_anotados" : []
    }
]
# Datos para Profesor
Profesor = {
    "Legajo" : 0,
    "Nombres" : "",
    "Apellido" : "",
    "Materias" : [
        # tuplas con el nombre de la materia y cantida de alumnos
    ],
}

