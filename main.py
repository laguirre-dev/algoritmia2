import os
from entidades.alumno.menu import menuAlumno
from entidades.profesor.menu import menuProfesor
from entidades.administrativo.menu import menuAdministrativo
from utils import pantalla, validaciones
from entidades import datos

# Configuración de rutas
CARPETA_UNIVERSIDADES = "universidades"

opciones_permitidas = [1, 2]

# Mapeo de roles a sus menús correspondientes
redireccion_menu = {
    "alumno": menuAlumno,
    "profesor": menuProfesor,
    "administrativo": menuAdministrativo,
}


def seleccionarUniversidad():
    """
    Lista los archivos JSON en la carpeta 'universidades' y permite elegir uno.
    Retorna la ruta completa del archivo seleccionado.
    """
    if not os.path.exists(CARPETA_UNIVERSIDADES):
        os.makedirs(CARPETA_UNIVERSIDADES)
        pantalla.red_text(
            f"Carpeta '{CARPETA_UNIVERSIDADES}' creada. Por favor coloque los archivos JSON ahí."
        )
        return None

    archivos = [f for f in os.listdir(CARPETA_UNIVERSIDADES) if f.endswith(".json")]

    if not archivos:
        pantalla.red_text(
            f"No se encontraron universidades (JSON) en la carpeta '{CARPETA_UNIVERSIDADES}'."
        )
        return None

    pantalla.limpiarTerminal()
    pantalla.header("SELECCIONAR UNIVERSIDAD")

    for i, archivo in enumerate(archivos, start=1):
        nombre_uni = archivo.replace(".json", "").replace("_", " ").upper()
        print(pantalla.Fore.CYAN + f"{i}. {nombre_uni}")

    print(pantalla.Fore.RED + f"{len(archivos) + 1}. Salir")

    opcion = validaciones.validaOpcion(list(range(1, len(archivos) + 2)))

    if opcion == len(archivos) + 1:
        return None

    archivo_seleccionado = archivos[opcion - 1]
    ruta_completa = os.path.join(CARPETA_UNIVERSIDADES, archivo_seleccionado)
    return ruta_completa


def main():
    while True:
        ruta_datos = seleccionarUniversidad()
    
        if not ruta_datos:
            pantalla.red_text("Saliendo del sistema...")
            break

        exito = datos.cargarDatosJson(ruta_datos)
        if not exito:
            return

        try:
            seleccion = pantalla.mostrarMenu("principal", opciones_permitidas)
            while seleccion != 2:
                validacion, rol, legajo = validaciones.validaLogin()

                if validacion:
                    try:
                        redireccion_menu[rol](legajo)
                    except Exception as e:
                        pantalla.red_text(f"Error al redirigir al menu: {e}")
                else:
                    pantalla.yellow_text(
                        "Ha superado el límite de intentos. Volviendo al menú principal..."
                    )

                seleccion = pantalla.mostrarMenu("principal", opciones_permitidas)

        except KeyboardInterrupt:
            pantalla.red_text("\n\nInterrupción detectada. Cerrando ordenadamente...")

        finally:
            pantalla.red_text("Guardando cambios y saliendo...")
            datos.guardarDatosJson()


if __name__ == "__main__":
    main()
