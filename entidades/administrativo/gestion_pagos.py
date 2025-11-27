"""
El objetivo del modulo es centralizar las funcionalidades sobre los pagos para los administrativos

Aprobacion y desaprobacion de pagos de alumnos
Enviar notificacion sobre pagos pendientes
Enviar notificacion pago rechazado
"""

from utils import pantalla, validaciones
from . import datos_backup2


def aprobarPago():
    """
    Aprueba el pago de un alumno (mueve de pendientes a pagadas).
    """
    pantalla.header("APROBAR PAGO")
    legajo = int(input("Ingrese el legajo del alumno: "))
    cuotas = [c for c in datos_backup2.CUOTAS_PENDIENTES if c["legajo"] == legajo]

    if not cuotas:
        pantalla.redText("El alumno no tiene pagos pendientes.")
        return

    print("Pagos pendientes:")
    for cuota in cuotas:
        print(f"Cuota N°{cuota['cuota_nro']}")

    nro = int(input("Ingrese el número de cuota a aprobar: "))
    cuota = next((c for c in cuotas if c["cuota_nro"] == nro), None)

    if cuota:
        datos_backup2.CUOTAS_PENDIENTES.remove(cuota)
        pantalla.greenText(f"Pago de cuota N°{nro} aprobado para el alumno {legajo}.")
    else:
        pantalla.redText("Número de cuota inválido.")




def menuGestionPagos():
    """
    Muestra el menu de gestion de pagos
    """
    pantalla.opcionesAdministrativoPagos()
    opcion = validaciones.validaOpcion([1, 2, 3])
