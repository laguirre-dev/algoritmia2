from entidades import alumno, profesor, administrativo
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
    pantalla.opcionesPrincipal()
    opcion = validaciones.validaOpcion(opciones_permitidas)
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
        opcion = validaciones.validaOpcion(opciones_permitidas)
    pantalla.redText("Saliendo del sistema...")
    datos.guardar_datos_json()
    sleep(2)


if __name__ == "__main__":
    main()
