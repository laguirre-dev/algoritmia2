# main.py
from entidades.alumno import menuAlumno
from entidades.profesor import menuProfesor
from entidades.administrativo import menuAdministrativo
from entidades.datos import CREDENCIALES
import os

# Cambiar el Menu con un Login de Usuario. Segun el ROL va a ir al menu correspondiente
""" Comentario de Prueba desde el usuario de Fede """

def limpiarTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrarMenu():
    """Muestra el menú principal."""
    print("---------------------------------")
    print("SISTEMA DE GESTIÓN DE ALUMNOS")
    print("---------------------------------")
    print("1. Iniciar sesión")
    print("2. Salir")
    print("---------------------------------")

def validarLegajo(legajo, clave):
    for credencial in CREDENCIALES:
        if credencial["legajo"] == legajo and credencial["clave"] == clave:
            return True, credencial["rol"]
        print("Las credenciales no son validas.")
        return False, False

def main():
    """Función principal del programa."""
    mostrarMenu()
    opcion = int(input("Seleccione una opción: "))
    while opcion != 2:
        intentos = 0
        validacion, rol = False, False
        while intentos < 3 and not validacion:
            legajo = int(input("Por favor, coloque su Legajo: "))
            clave = input("Por favor, escriba su clave para ingresar: ")
            validacion, rol = validarLegajo(legajo, clave)
            intentos += 1
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
        if intentos >= 3:
            limpiarTerminal()
            print("Ha superado el limite de intentos. Volviendo al menu principal...")
            input("Presione Enter para avanzar")
        mostrarMenu()
        opcion = int(input("Seleccione una opción: "))
    print("Saliendo del sistema...")
    # Le agrego esto para mostrar el mensaje de salida
    input("Presione Enter para salir")


main()
