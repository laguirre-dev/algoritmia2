from entidades import datos
from utils import pantalla


def crearClave(legajo, nombre, apellido):
    parte1 = str(legajo)
    parte2 = nombre[0].upper()
    parte3 = apellido.lower()
    return parte1 + parte2 + parte3


def login(legajo, clave):
    for credencial in datos.sistema["CREDENCIALES"]:
        if credencial["legajo"] == legajo and credencial["clave"] == clave:
            return True, credencial["rol"]
    pantalla.red_text("Credenciales incorrectas. Intentelo nuevamente.")
    return False, False


def modificaClaveCredenciales(legajo, clave, rol, base_de_datos):
    encontrado = False
    for credencial in base_de_datos:
        if credencial["legajo"] == legajo and credencial["rol"] == rol:
            credencial["clave"] = clave
            pantalla.header("CREDENCIALES REESTABLECIDAS CON EXITO")
            encontrado = True
    if not encontrado:
        pantalla.red_text("No se encontro el usuario.")
        return
    return
