from entidades import datos
from entidades.alumno import menuAlumno
from entidades.profesor import menuProfesor
from entidades.administrativo import menuAdministrativo
from utils import pantalla, validaciones
from time import sleep

redireccion_menu = {
    "alumno": menuAlumno,
    "profesor": menuProfesor,
    "administrativo": menuAdministrativo,
}


def main():
    pantalla.opcionesPrincipal()
    opcion = validaciones.validaOpcion(redireccion_menu.keys())
    while opcion != 2:
        validacion, rol, legajo = validaciones.validaLogin()
        if validacion:
            try:
                redireccion_menu[rol](legajo)
            except Exception as e:
                pantalla.redText(f"Error al redirigir al menu: {e}")
                sleep(2)
        else:
            pantalla.yellowText(
                "Ha superado el límite de intentos. Volviendo al menú principal..."
            )
            sleep(2)
        pantalla.opcionesPrincipal()
        opcion = validaciones.validaOpcion(redireccion_menu.keys())
    pantalla.redText("Saliendo del sistema...")
    datos.guardar_datos_json()
    sleep(2)


if __name__ == "__main__":
    main()
