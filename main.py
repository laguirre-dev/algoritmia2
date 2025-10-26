from entidades.alumno.menuAlumno import menuAlumno
from entidades.profesor.menuProfesor import menuProfesor
from entidades.administrativo.menu import menuAdministrativo
import utils.pantalla as headers
import utils.credenciales as credenciales

def mostrarMenu():
    headers.header("SISTEMA DE GESTIÓN DE ALUMNOS")
    print(headers.Fore.GREEN + "1. Iniciar sesión")
    print(headers.Fore.RED   + "2. Salir")
    print(headers.Fore.GREEN + "-" * 50)

def main():
    mostrarMenu()
    try:
        opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
    except ValueError:
        opcion = 0

    while opcion != 2:
        intentos = 0
        validacion, rol = False, False

        while intentos < 3 and not validacion:
            try:
                legajo = int(input(headers.Fore.WHITE + "Por favor, coloque su Legajo: "))
            except ValueError:
                print(headers.Fore.RED + "El legajo debe ser numérico.")
                intentos += 1
                continue

            clave = input(headers.Fore.WHITE + "Por favor, escriba su clave para ingresar: ")

            try:
                validacion, rol = credenciales.login(legajo, clave)
            except Exception as e:
                print(headers.Fore.RED + f"Error en la validación: {e}")
                validacion, rol = False, False
            intentos += 1

        if validacion:
            try:
                if rol == "alumno":
                    headers.limpiarTerminal()
                    headers.header("MENÚ ALUMNO")
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
                    print(headers.Fore.RED + "Rol no reconocido.")
            except Exception as e:
                print(headers.Fore.RED + f"Error al cargar el menú: {e}")
        else:
            if intentos >= 3:
                headers.limpiarTerminal()
                print(headers.Fore.RED + "Ha superado el límite de intentos. Volviendo al menú principal...")
                input(headers.Fore.WHITE + "Presione Enter para avanzar")

        mostrarMenu()
        try:
            opcion = int(input(headers.Fore.WHITE + "Seleccione una opción: "))
        except ValueError:
            opcion = 0

    print(headers.Fore.RED + headers.Style.BRIGHT + "Saliendo del sistema...")
    input(headers.Fore.WHITE + "Presione Enter para salir")

if __name__ == "__main__":
    main()