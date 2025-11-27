"""
Opciones disponibles:
1. Sumar Pago Pendiente
2. Generar reporte de Deudores
3. Volver al menú principal
"""

from tabulate import tabulate
from datetime import date
from reportes import generador_de_reportes
from utils import pantalla, validaciones
from entidades.administrativo import menuAdministrativo
from entidades import datos


def sumarPagoPendiente():
    """
    Realiza un append a la lista de pagos pendientes
    """
    try:
        legajo = int(input("Ingrese el legajo del alumno: "))
        cuota = int(input("Ingrese el nro de cuota pendiente del alumno: "))
    except ValueError:
        print("Introdujo un valor no valido. Debe ser numerico.")
        return
    # revisar que la cuota no este en la lista
    for cuota in datos.CUOTAS_PENDIENTES:
        if cuota["cuota_nro"] == cuota and cuota["legajo"] == legajo:
            print("La cuota ya esta en la lista de pagos pendientes para ese Alumno.")
            return
    datos.CUOTAS_PENDIENTES.append(
        {
            "cuota_nro": cuota,
            "legajo": legajo,
        }
    )
    print("Pago pendiente sumado con exito.")
    return


def generarReporteDeudores():
    """
    Genera un txt con la lista de deudores, su cuota y el monto pendiente. Hace la busqueda en la base de datos pagos pendientes
    """
    print("Opcion: Generar reporte de deudores")
    cuotasPendientes = [
        [cuota["cuota_nro"], cuota["legajo"]] for cuota in datos.CUOTAS_PENDIENTES
    ]
    print(tabulate(cuotasPendientes, headers=["Cuota", "Legajo"]))
    fecha = date.today()
    nombre_archivo = f"reporte_cuotas_pendientes_{fecha}"
    generador_de_reportes.guardarReporte(nombre_archivo, cuotasPendientes)
    return


logica_seleccion_menu = {
    1: sumarPagoPendiente,
    2: generarReporteDeudores,
    3: menuAdministrativo,
}


def menuGestionPagos():
    """Muestra el menu de opciones de un Administrativo en la gestion de pagos"""
    pantalla.opcionesAdministrativoPagos()
    opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    while opcion != 0:
        logica_seleccion_menu[opcion]()
        pantalla.opcionesAdministrativoPagos()
        opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    return
