from utils import pantalla, credenciales

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


def insertaCredenciales(datos_usuario, base_de_datos):
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
        base_de_datos.append(credencial_creada)
        pantalla.header("CREDENCIALES CREADAS CON EXITO")
        return True
    except Exception as e:
        print(e)
        return False