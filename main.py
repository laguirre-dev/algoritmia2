from entidades.alumno import menuAlumno as alumno
from entidades.profesor import menuProfesor as profesor
from entidades.administrativo import menuAdministrativo as administrativo
from utils import pantalla, validaciones
from entidades import datos
from time import sleep

opciones_permitidas = [1, 2]
redireccion_menu = {
    "alumno": alumno.menuAlumno,
    "profesor": profesor.menuProfesor,
    "administrativo": administrativo.menuAdministrativo,
}


def main():
    seleccion = pantalla.mostrar_menu("principal", opciones_permitidas)
    while seleccion != 2:
        validacion, rol, legajo = validaciones.valida_login()
        if validacion:
            try:
                redireccion_menu[rol](legajo)
            except Exception as e:
                pantalla.red_text(f"Error al redirigir al menu: {e}")
                sleep(2)
        else:
            pantalla.yellow_text(
                "Ha superado el límite de intentos. Volviendo al menú principal..."
            )
            sleep(2)
        seleccion = pantalla.mostrar_menu("principal", opciones_permitidas)
    pantalla.red_text("Saliendo del sistema...")
    datos.guardar_datos_json()
    sleep(2)


if __name__ == "__main__":
    main()
