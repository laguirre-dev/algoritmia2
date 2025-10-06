from entidades.alumno import menuAlumno
from entidades.profesor import menuProfesor
from entidades.administrativo import menuAdministrativo
from entidades.datos import CREDENCIALES
import os

def limpiarTerminal():
    # Funcion para limpiar la terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrarMenu():
    # Funcion para mostrar las opciones del menu
    print("---------------------------------")
    print("SISTEMA DE GESTIÓN DE ALUMNOS")
    print("---------------------------------")
    print("1. Iniciar sesión")
    print("2. Salir")
    print("---------------------------------")

def login(legajo, clave):
    # funcion para validar login, devuelve si es valido y el rol
    for credencial in CREDENCIALES:
        if credencial["legajo"] == legajo and credencial["clave"] == clave:
            return True, credencial["rol"]
    print("Credenciales incorrectas. Intentelo nuevamente.")
    return False, False

def main():
    # funcion del programa
    mostrarMenu()
    # muestra menu y pide indicar una opcion
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        opcion = 0

    while opcion != 2:
        intentos = 0
        validacion, rol = False, False
        while intentos < 3 and not validacion:
            try:
                legajo = int(input("Por favor, coloque su Legajo: "))
            except ValueError:
                print("El legajo debe ser numérico.")
                intentos += 1
                continue
            clave = input("Por favor, escriba su clave para ingresar: ")
            validacion, rol = login(legajo, clave)
            intentos += 1

        if validacion:
            if rol == "alumno":
                limpiarTerminal()
                print("¡Bienvenido Alumno!")
                menuAlumno(legajo)
            elif rol == "profesor":
                limpiarTerminal()
                print("¡Bienvenido Profesor!")
                menuProfesor(legajo)
            elif rol == "administrativo":
                limpiarTerminal()
                print("¡Bienvenido!")
                menuAdministrativo()
        else:
            if intentos >= 3:
                limpiarTerminal()
                print("Ha superado el limite de intentos. Volviendo al menu principal...")
                input("Presione Enter para avanzar")

        mostrarMenu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            opcion = 0

    print("Saliendo del sistema...")
    # Le agrego esto para mostrar el mensaje de salida
    input("Presione Enter para salir")

if __name__ == "__main__":
    main()