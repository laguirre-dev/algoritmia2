from utils import pantalla, credenciales
from time import sleep


def valida_opcion(opciones_permitidas):
    opcion = 0
    while opcion not in opciones_permitidas:
        try:
            opcion = int(input(pantalla.bold_text("Seleccione una opción: ")))
        except ValueError:
            pantalla.yellow_text("Opción no válida. Intente nuevamente.\n")
    return opcion


def valida_login():
    intentos = 0
    validacion, rol, legajo = False, False, False
    reintentar = False
    while intentos < 3 and not validacion and not reintentar:
        try:
            legajo = int(input("Por favor, coloque su legajo: "))
        except ValueError:
            pantalla.redText("El legajo debe ser numérico.")
            intentos += 1
            reintentar = True
        clave = input("Por favor, escriba su clave para ingresar: ")
        try:
            validacion, rol = credenciales.login(legajo, clave)
        except Exception as e:
            pantalla.redText(f"Error en la validación: {e}")
            validacion, rol = False, False
        intentos += 1
    return validacion, rol, legajo
