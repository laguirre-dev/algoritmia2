def mostrar_menu():
    """
    Función que muestra el menú principal del sistema.
    """
    print("---------------------------------")
    print("SISTEMA DE GESTIÓN DE ALUMNOS")
    print("---------------------------------")
    print("1. Iniciar sesión como Alumno")
    print("2. Iniciar sesión como Profesor")
    print("3. Iniciar sesión como Administrativo")
    print("4. Salir")
    print("---------------------------------")

def main():
    """
    Función principal del programa.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Funcionalidad de Alumno en desarrollo...")
        elif opcion == '2':
            print("Funcionalidad de Profesor en desarrollo...")
        elif opcion == '3':
            print("Funcionalidad de Administrativo en desarrollo...")
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()