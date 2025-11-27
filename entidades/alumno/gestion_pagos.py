from entidades import datos as datos
from utils import pantalla as headers
from utils import busquedas as busqueda
from reportes import generador_de_reportes
from colorama import Fore
from datetime import datetime

def consultarPagos(legajoAlumno):
    """
    Muestra las cuotas pendientes de un alumno.
    """
    alumno = busqueda.buscarAlumnoPorLegajo(legajoAlumno)
    if not alumno:
        print(Fore.RED + "Alumno no encontrado.")
        return
    
    if datos.sistema["CUOTAS_PENDIENTES"] is None:
        datos.sistema["CUOTAS_PENDIENTES"] = []

    pendientes = [c for c in datos.sistema["CUOTAS_PENDIENTES"] if c["legajo"] == legajoAlumno]
    headers.header("CONSULTA DE PAGOS")

    if not pendientes:
        print(Fore.GREEN + f"El alumno {alumno['nombre']} {alumno['apellido']} no tiene pagos pendientes.")
    else:
        print(Fore.YELLOW + f"Pagos pendientes de {alumno['nombre']} {alumno['apellido']}:")
        for i, pago in enumerate(pendientes, start=1):
            print(Fore.WHITE + f"{i}. Cuota Nro: {pago['cuota_nro']}")


def pagarCuotasAdeudadas(legajoAlumno):
    alumno = busqueda.buscarAlumnoPorLegajo(legajoAlumno)
    if not alumno:
        print(Fore.RED + "Alumno no encontrado.")
        return

    pendientes = [c for c in datos.sistema["CUOTAS_PENDIENTES"] if c["legajo"] == legajoAlumno]
    headers.header("PAGO DE CUOTAS")

    if not pendientes:
        print(Fore.GREEN + f"{alumno['nombre']} {alumno['apellido']} no tiene cuotas adeudadas.")
        return

    print(Fore.YELLOW + f"Cuotas pendientes de {alumno['nombre']} {alumno['apellido']}:")
    for i, pago in enumerate(pendientes, start=1):
        print(Fore.WHITE + f"{i}. Cuota Nro: {pago['cuota_nro']}")

    seleccion = input(Fore.WHITE + "Ingrese los números de las cuotas que desea pagar (separados por coma): ")

    try:
        indices = [int(x.strip()) for x in seleccion.split(",")]
    except ValueError:
        print(Fore.RED + "Entrada inválida. Debe ingresar números separados por coma.")
        return

    pagadas = []
    for idx in indices:
        if 1 <= idx <= len(pendientes):
            pagadas.append(pendientes[idx - 1])

    if not pagadas:
        print(Fore.RED + "No se seleccionaron cuotas válidas.")
        return

    datos.sistema["CUOTAS_PENDIENTES"] = [c for c in datos.sistema["CUOTAS_PENDIENTES"]if c not in pagadas]

    print(Fore.GREEN + "Se han abonado las siguientes cuotas:")
    for pago in pagadas:
        print(Fore.WHITE + f"- Cuota Nro: {pago['cuota_nro']}")

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    nombre_archivo = f"Recibo_Cuotas_{alumno['legajo']}"
    contenido = [
        {"Alumno": f"{alumno['nombre']} {alumno['apellido']}", "Legajo": alumno["legajo"], "Fecha": fecha}
    ]
    for pago in pagadas:
        contenido.append({"Cuota abonada": pago["cuota_nro"]})

    generador_de_reportes.guardarReporte(nombre_archivo, contenido)
    print(Fore.GREEN + f"Se generó el recibo de cuotas: {nombre_archivo}.txt")