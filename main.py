# main.py

import algoritmia2.entidades.alumno as alumno
import algoritmia2.entidades.profesor as profesor
import algoritmia2.entidades.administrativo as administrativo

def mostrarMenu():
    """Muestra el menú principal."""
    print("---------------------------------")
    print("SISTEMA DE GESTIÓN DE ALUMNOS")
    print("---------------------------------")
    print("1. Iniciar sesión como Alumno")
    print("2. Iniciar sesión como Profesor")
    print("3. Iniciar sesión como Administrativo")
    print("4. Salir")
    print("---------------------------------")

def main():
    """Función principal del programa."""
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alumno.menuAlumno()
        elif opcion == '2':
            profesor.menuProfesor()
        elif opcion == '3':
            administrativo.menuAdministrativo()
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()