from entidades.alumno.menuAlumno import menuAlumno
from entidades.profesor.menuProfesor import menuProfesor
from entidades.administrativo.menu import menuAdministrativo
import utils.pantalla as headers
import utils.credenciales as credenciales
import sys
import os

sys.path.append(os.path.dirname(__file__))

def mostrarMenu():
    # Funcion para mostrar las opciones del menu
    headers.header("SISTEMA DE GESTIÓN DE ALUMNOS")
    print(headers.Fore.GREEN + "1. Iniciar sesión")
    print(headers.Fore.RED   + "2. Salir")
    print(headers.Fore.GREEN + "-" * 50)

def main():
    mostrarMenu()
    opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))

    while opcion != 2:
        intentos = 0
        validacion, rol = False, False
        while intentos < 3 and not validacion:
            legajo = int(input(headers.Fore.WHITE + "Por favor, coloque su Legajo: "))
            clave = input(headers.Fore.WHITE + "Por favor, escriba su clave para ingresar: ")
            validacion, rol = credenciales.login(legajo, clave)
            intentos += 1

        if validacion:
            if rol == "alumno":
                headers.limpiarTerminal()
                headers.header("MENÚ ALUMNO")
                print(headers.Fore.GREEN + "¡Bienvenido Alumno!")
                menuAlumno(legajo)
            elif rol == "profesor":
                headers.limpiarTerminal()
                headers.header("MENÚ PROFESOR")
                menuProfesor(legajo)
            elif rol == "administrativo":
                headers.limpiarTerminal()
                headers.header("MENÚ ADMINISTRATIVO")
                print(headers.Fore.GREEN + "¡Bienvenido Administrativo!")
                menuAdministrativo()
        else:
            if intentos >= 3:
                headers.limpiarTerminal()
                print(headers.Fore.RED + "Ha superado el limite de intentos. Volviendo al menu principal...")
                input(headers.Fore.WHITE + "Presione Enter para avanzar")

        mostrarMenu()
        opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))

    print(headers.Fore.RED + headers.Style.BRIGHT + "Saliendo del sistema...")
    input(headers.Fore.WHITE + "Presione Enter para salir")

if __name__ == "__main__":
    main()