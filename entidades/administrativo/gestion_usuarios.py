# Objetivo del modulo: Centralizar logica de ABM de usuarios
import entidades.datos as datos
from utils import credenciales, pantalla


def inserta_usuario(datos_usuario, base_de_datos):
    """
    Genera un alumno o profesor segun el rol y la base de datos recibida
    """
    legajo, nombre, apellido, rol = datos_usuario
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
        pantalla.imprime_datos(usuario)
    except Exception as e:
        print(e)
    return


def inserta_credenciales(datos_usuario):
    """
    Crea credenciales nuevas segun el rol y los datos del usuario
    """
    legajo, nombre, apellido, rol = datos_usuario
    clave = credenciales.crear_clave(legajo, nombre, apellido)
    credencial_creada = {"legajo": legajo, "clave": clave, "rol": rol}
    try:
        datos.CREDENCIALES.append(credencial_creada)
        pantalla.header("CREDENCIALES CREADAS CON EXITO")
        pantalla.imprime_datos(credencial_creada)
    except Exception as e:
        print(e)
    return


def registrar_usuario(rol):
    """
    Realiza el registro de un usuario usando funciones externas de insertar usuario y credenciales
    """
    legajo = max([alumno["legajo"] for alumno in datos.ALUMNOS_DB], default=100) + 1
    print(f"Legajo: {legajo}")
    nombre = input("Ingrese el Nombre del ingresante: ")
    apellido = input("Ingrese el Apellido del ingresante: ")
    usuario = (legajo, nombre, apellido, rol)
    if rol == "alumno":
        inserta_usuario(usuario, datos.ALUMNOS_DB)
        inserta_credenciales(usuario)
    else:
        inserta_usuario(usuario, datos.PROFESORES_DB)
        inserta_credenciales(usuario)
    return

def menu_gestion_alumnos():
    return