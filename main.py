from entidades.alumno import menuAlumno
from entidades.profesor import menuProfesor
from entidades.administrativo import menuAdministrativo
from entidades.datos import CREDENCIALES
from colorama import init, Fore, Style
import os

# Inicializamos colorama
init(autoreset=True)

def limpiarTerminal():
    # Funcion para limpiar la terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def header(titulo):
    # Encabezado estilizado con onda universitaria
    print(Fore.GREEN + "=" * 50)
    print(Style.BRIGHT + Fore.WHITE + titulo.center(50))
    print(Fore.GREEN + "=" * 50)

def mostrarMenu():
    # Funcion para mostrar las opciones del menu
    header("SISTEMA DE GESTIÓN DE ALUMNOS")
    print(Fore.GREEN + "1. Iniciar sesión")
    print(Fore.RED + "2. Salir")
    print(Fore.GREEN + "-" * 50)

def login(legajo, clave):
    # funcion para validar login, devuelve si es valido y el rol
    for credencial in CREDENCIALES:
        if credencial["legajo"] == legajo and credencial["clave"] == clave:
            return True, credencial["rol"]
    print(Fore.RED + "Credenciales incorrectas. Intentelo nuevamente.")
    return False, False

def main():
    # funcion del programa
    mostrarMenu()
    opcion = int(input(Fore.WHITE + "Seleccione una opción: "))

    while opcion != 2:
        intentos = 0
        validacion, rol = False, False
        while intentos < 3 and not validacion:
            legajo = int(input(Fore.WHITE + "Por favor, coloque su Legajo: "))
            clave = input(Fore.WHITE + "Por favor, escriba su clave para ingresar: ")
            validacion, rol = login(legajo, clave)
            intentos += 1

        if validacion:
            if rol == "alumno":
                limpiarTerminal()
                header("MENÚ ALUMNO")
                print(Fore.GREEN + "¡Bienvenido Alumno!")
                menuAlumno(legajo)
            elif rol == "profesor":
                limpiarTerminal()
                header("MENÚ PROFESOR")
                print(Fore.GREEN + "¡Bienvenido Profesor!")
                menuProfesor(legajo)
            elif rol == "administrativo":
                limpiarTerminal()
                header("MENÚ ADMINISTRATIVO")
                print(Fore.GREEN + "¡Bienvenido Administrativo!")
                menuAdministrativo()
        else:
            if intentos >= 3:
                limpiarTerminal()
                print(Fore.RED + "Ha superado el limite de intentos. Volviendo al menu principal...")
                input(Fore.WHITE + "Presione Enter para avanzar")

        mostrarMenu()
        opcion = int(input(Fore.WHITE + "Seleccione una opción: "))

    print(Fore.RED + Style.BRIGHT + "Saliendo del sistema...")
    input(Fore.WHITE + "Presione Enter para salir")

if __name__ == "__main__":
    main()