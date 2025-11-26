from utils import pantalla, validaciones
from . import gestion_cursos, gestion_pagos, gestion_usuarios
import main as app

logica_seleccion_menu = {
    1: gestion_usuarios.menuGestionUsuarios,
    2: gestion_cursos.menuGestionCursos,
    3: gestion_pagos.menuGestionPagos,
    4: app.main,
}


def menuAdministrativo(legajo):
    """Muestra el menú de opciones para un Administrativo."""
    pantalla.greenText(f"Hola administrativo: {legajo}")
    pantalla.opcionesAdministrativoPrincipal()
    opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    while opcion != 4:
        logica_seleccion_menu[opcion]()
        pantalla.opcionesAdministrativoPrincipal()
        opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    return
