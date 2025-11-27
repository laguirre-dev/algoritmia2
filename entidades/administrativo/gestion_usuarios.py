"""
opciones disponibles
1. Agregar Alumno
2. Agregar Profesor
3. Reestablecer credenciales
3. Volver al menu anterior
"""

from entidades.datos import sistema
from utils import pantalla, modificadores, credenciales, validaciones

roles_disponibles = {
    1: "alumno",
    2: "profesor",
}


def registrarUsuario(rol, base_de_datos):
    """
    Logica de insercion de alumno o profesor segun corresponda, y creacion de credenciales del mismo
    """
    legajo = max([usuario["legajo"] for usuario in base_de_datos]) + 1
    print(f"Legajo: {legajo}")
    nombre = input("Ingrese el Nombre del ingresante: ")
    while not validaciones.validaTextoRegex(nombre):
        pantalla.redText("El Nombre debe contener solo letras.")
        nombre = input("Ingrese un Nombre Valido: ")
    apellido = input("Ingrese el Apellido del ingresante: ")
    while not validaciones.validaTextoRegex(apellido):
        pantalla.redText("El Apellido debe contener solo letras.")
        apellido = input("Ingrese un Apellido Valido: ")
    usuario = (legajo, nombre, apellido, rol)
    modificadores.insertaUsuario(usuario, base_de_datos)
    modificadores.insertaCredenciales(usuario, sistema["CREDENCIALES"])
    return


def agregarAlumno():
    """
    Ejecuta registrarUsuario pero con rol = "alumno"
    """
    registrarUsuario("alumno", sistema["ALUMNOS_BD"])
    return


def agregarProfesor():
    """
    Ejecuta registrarUsuario pero con rol = "profesor"
    """
    registrarUsuario("profesor", sistema["PROFESORES_BD"])
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
        return
    print("Seleccione el rol correspondiente (indique el numero): ")
    print("1. Alumno")
    print("2. Profesor")
    try:
        rol = roles_disponibles.get(int(input("Opcion: ")))
    except ValueError:
        pantalla.redText("La opcion debe ser numérica.")
    clave = input("Ingrese la nueva clave (Ejemplo: Asdf1!): ")
    credenciales.modificaClaveCredenciales(legajo, clave, rol, sistema["CREDENCIALES"])
    return


logica_seleccion_menu = {
    1: agregarAlumno,
    2: agregarProfesor,
    3: reestablecerCredenciales,
    4: "Volver al menu anterior",
}


def menuGestionUsuarios():
    """Muestra el submenu de Administrativo: Gestion de Usuarios"""
    pantalla.opcionesAdministrativoUsuarios()
    opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    while opcion != 4:
        logica_seleccion_menu[opcion]()
        pantalla.opcionesAdministrativoUsuarios()
        opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    return
