from entidades.datos import CREDENCIALES
import utils.pantalla as headers

def crear_clave(legajo, nombre, apellido):
    parte1 = str(legajo)
    parte2 = nombre[0].upper()
    parte3 = apellido.lower()
    return parte1 + parte2 + parte3

def login(legajo, clave):
    for credencial in CREDENCIALES:
        if credencial["legajo"] == legajo and credencial["clave"] == clave:
            return True, credencial["rol"]
    print(headers.Fore.RED + "Credenciales incorrectas. Intentelo nuevamente.")
    return False, False

def imprimir_credenciales(legajo, clave):
    print("\n#####################")
    print("Legajo: ", legajo)
    print("Clave: ", clave)
    print("#####################\n")
