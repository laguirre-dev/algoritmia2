# Objetivo del modulo: Centralizar logica de ABM de usuarios
import entidades.datos as datos
from utils import credenciales, pantalla


def insertaUsuario(datos_usuario, base_de_datos):
    """
    Genera un alumno o profesor segun el rol y la base de datos recibida
    """
    try:
        legajo, nombre, apellido, rol = datos_usuario
    except Exception as e:
        print("Faltan datos para crear credenciales, {e}")
        return False
    if rol == "alumno":
        usuario = {
            "legajo": legajo,
            "nombre": nombre,
            "apellido": apellido,
            "cursos": [],
            "pagos_pendientes": [],
        }
    else:
        usuario = {
            "legajo": legajo,
            "nombre": nombre,
            "apellido": apellido,
            "materias": [],
        }
    try:
        base_de_datos.append(usuario)
        pantalla.header("USUARIO REGISTRADO CON EXITO")
        return True
    except Exception as e:
        print(e)
        return False


def insertaCredenciales(datos_usuario):
    """
    Crea credenciales nuevas segun el rol y los datos del usuario
    """
    try:
        legajo, nombre, apellido, rol = datos_usuario
    except Exception as e:
        print("Faltan datos para crear credenciales, {e}")
        return False
    clave = credenciales.crearClave(legajo, nombre, apellido)
    credencial_creada = {"legajo": legajo, "clave": clave, "rol": rol}
    try:
        datos.CREDENCIALES.append(credencial_creada)
        pantalla.header("CREDENCIALES CREADAS CON EXITO")
        return True
    except Exception as e:
        print(e)
        return False


def registrarUsuario(rol):
    """
    Realiza el registro de un usuario usando funciones externas de insertar usuario y credenciales
    """
    legajo = max([alumno["legajo"] for alumno in datos.ALUMNOS_DB], default=100) + 1
    print(f"Legajo: {legajo}")
    nombre = input("Ingrese el Nombre del ingresante: ")
    apellido = input("Ingrese el Apellido del ingresante: ")
    usuario = (legajo, nombre, apellido, rol)
    if rol == "alumno":
        insertaUsuario(usuario, datos.ALUMNOS_DB)
        insertaCredenciales(usuario)
    else:
        insertaUsuario(usuario, datos.PROFESORES_DB)
        insertaCredenciales(usuario)
    return


def menuGestionUsuarios():
    return
