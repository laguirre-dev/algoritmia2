from utils import pantalla, validaciones
from entidades.administrativo.gestion_cursos import menuGestionCursos
from entidades.administrativo.gestion_pagos import menuGestionPagos
from entidades.administrativo.gestion_usuarios import menuGestionUsuarios

logica_seleccion_menu = {
    1: menuGestionUsuarios,
    2: menuGestionCursos,
    3: menuGestionPagos,
    4: "Volver al menu principal",
}


def menuAdministrativo(legajo=1):
    """
    Muestra el menú de opciones para un Administrativo.
    """
    print("Bienvenido Administrativo: ", legajo)
    pantalla.opcionesAdministrativoPrincipal()
    opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    while opcion != 4:
        logica_seleccion_menu[opcion]()
        pantalla.opcionesAdministrativoPrincipal()
        opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    return
