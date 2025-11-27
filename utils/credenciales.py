from entidades import datos
from utils import pantalla


def crearClave(legajo, nombre, apellido):
    parte1 = str(legajo)
    parte2 = nombre[0].upper()
    parte3 = apellido.lower()
    return parte1 + parte2 + parte3


def modificaClaveCredenciales(legajo, clave, rol, base_de_datos):
    """
    Reestablece las credenciales del usuario
    """
    encontrado = False
    for credencial in base_de_datos:
        if credencial["legajo"] == legajo and credencial["rol"] == rol:
            credencial["clave"] = clave
            pantalla.greenText("¡CREDENCIALES MODIFICADAS CON EXITO!")
            pantalla.yellowText(
                "Alumno: ", credencial["legajo"], ";Clave: ", credencial["clave"]
            )
            encontrado = True
    if not encontrado:
        pantalla.redText("Legajo no encontrado. Intente nuevamente.")
    return True


def login(legajo, clave):
    for credencial in datos.CREDENCIALES:
        if credencial["legajo"] == legajo and credencial["clave"] == clave:
            return True, credencial["rol"]
    pantalla.redText("Credenciales incorrectas. Intentelo nuevamente.")
    return False, False
