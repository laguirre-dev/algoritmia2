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
from entidades import datos


def sumarPagoPendiente():
    """
    Realiza un append a la lista de pagos pendientes
    """
    try:
        ingreso_legajo = int(input("Ingrese el legajo del alumno: "))
        ingreso_cuota = int(input("Ingrese el nro de cuota pendiente del alumno: "))
    except ValueError:
        print("Introdujo un valor no valido. Debe ser numerico.")
        return
    # revisar que la cuota no este en la lista
    for cuota in datos.sistema["CUOTAS_PENDIENTES"]:
        if cuota["cuota_nro"] == ingreso_cuota and cuota["legajo"] == ingreso_legajo:
            pantalla.redText("La cuota ya esta en la lista de pagos pendientes para ese Alumno.")
            return
    datos.sistema["CUOTAS_PENDIENTES"].append(
        {
            "cuota_nro": ingreso_cuota,
            "legajo": ingreso_legajo,
        }
    )

    pantalla.greenText("Pago pendiente sumado con exito.")
    return


def generarReporteDeudores():
    """
    Genera un txt con la lista de deudores, su cuota y el monto pendiente. Hace la busqueda en la base de datos pagos pendientes
    """
    print("Opcion: Generar reporte de deudores")
    cuotasPendientes = [
        {"cuota_nro": cuota["cuota_nro"], "legajo": cuota["legajo"]}
        for cuota in datos.sistema["CUOTAS_PENDIENTES"]
    ]
    fecha = date.today()
    nombre_archivo = f"reporte_cuotas_pendientes_{fecha}"
    generador_de_reportes.guardarReporte(nombre_archivo, cuotasPendientes)
    return


logica_seleccion_menu = {
    1: sumarPagoPendiente,
    2: generarReporteDeudores,
    3: "Volver al menu anterior",
}


def menuGestionPagos():
    """Muestra el menu de opciones de un Administrativo en la gestion de pagos"""
    pantalla.opcionesAdministrativoPagos()
    opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    while opcion != 3:
        logica_seleccion_menu[opcion]()
        pantalla.opcionesAdministrativoPagos()
        opcion = validaciones.validaOpcion(logica_seleccion_menu.keys())
    return
