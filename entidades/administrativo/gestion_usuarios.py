"""
opciones disponibles
1. Agregar Alumno
2. Agregar Profesor
3. Reestablecer credenciales
3. Volver al menu anterior
"""

from entidades import datos
from utils import pantalla, modificadores, credenciales, validaciones
from entidades.administrativo import menuAdministrativo

roles_disponibles = {
    1: "alumno",
    2: "profesor",
}


def registrarUsuario(rol):
    """
    Logica de insercion de alumno o profesor segun corresponda, y creacion de credenciales del mismo
    """
    legajo = max([alumno["legajo"] for alumno in datos.ALUMNOS_DB], default=100) + 1
    print(f"Legajo: {legajo}")
    nombre = input("Ingrese el Nombre del ingresante: ")
    apellido = input("Ingrese el Apellido del ingresante: ")
    usuario = (legajo, nombre, apellido, rol)
    if rol == "alumno":
        modificadores.insertaUsuario(usuario, datos.ALUMNOS_DB)
        modificadores.insertaCredenciales(usuario, datos.CREDENCIALES)
    else:
        modificadores.insertaUsuario(usuario, datos.PROFESORES_DB)
        modificadores.insertaCredenciales(usuario, datos.CREDENCIALES)
    return


def agregarAlumno():
    """
    Ejecuta registrarUsuario pero con rol = "alumno"
    """
    registrarUsuario("alumno")
    return


def agregarProfesor():
    """
    Ejecuta registrarUsuario pero con rol = "profesor"
    """
    registrarUsuario("profesor")
    return


def reestablecerCredenciales():
    """
    Modifica la clave de un usuario, solicita legajo, rol y clave nueva
    """
    pantalla.greenText("- REESTABLECER CREDENCIALES")
    try:
        legajo = int(input("Ingrese el legajo del usuario: "))
    except ValueError:
        pantalla.redText("El legajo debe ser numérico.")
    print("Seleccione el rol correspondiente (indique el numero): ")
    print("1. Alumno")
    print("2. Profesor")
    try:
        rol = roles_disponibles.get(int(input("Opcion: ")))
    except ValueError:
        pantalla.redText("La opcion debe ser numérica.")
    clave = input("Ingrese la nueva clave (Ejemplo: Asdf1!): ")
    credenciales.modificaClaveCredenciales(legajo, clave, rol, datos.CREDENCIALES)
    return


logica_seleccion_menu = {
    1: agregarAlumno,
    2: agregarProfesor,
    3: reestablecerCredenciales,
    4: menuAdministrativo,
}


def menuGestionUsuarios():
    """Muestra el submenu de Administrativo: Gestion de Usuarios"""
    pantalla.opcionesAdministrativoUsuarios()
    opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    while opcion != logica_seleccion_menu.keys()[-1]:
        logica_seleccion_menu[opcion]()
        pantalla.opcionesAdministrativoUsuarios()
        opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    return
