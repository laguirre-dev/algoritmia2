from utils import pantalla, credenciales
import re 

def validaOpcion(opciones_permitidas):
    opcion = 0
    while opcion not in opciones_permitidas:
        try:
            opcion = int(input(pantalla.bold_text("Seleccione una opción: ")))
        except ValueError:
            pantalla.yellow_text("Opción no válida. Intente nuevamente.\n")
    return opcion

def validaLogin():
    intentos = 0
    validacion, rol, legajo = False, False, False
    reintentar = False
    
    while intentos < 3 and not validacion:
        reintentar = False 
        try:
            input_legajo = input("Por favor, coloque su legajo: ")
            
            if not input_legajo.isdigit():
                pantalla.red_text("El legajo debe ser numérico.")
                intentos += 1
                continue
                
            legajo = int(input_legajo)
            
        except ValueError:
            pantalla.red_text("Error en el formato del legajo.")
            intentos += 1
            continue

        clave = input("Por favor, escriba su clave para ingresar: ")
        
        try:
            validacion, rol = credenciales.login(legajo, clave)
            if not validacion:
                intentos += 1
        except Exception as e:
            pantalla.red_text(f"Error en la validación: {e}")
            validacion, rol = False, False
            intentos += 1
            
    return validacion, rol, legajo


def validaTextoRegex(texto, tipo="nombre"):
    """
    Valida nombres o apellidos usando Expresiones Regulares.
    Permite letras y espacios, pero no números ni símbolos raros.
    """
    if tipo == "nombre":
        patron = r"^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$"
        if re.match(patron, texto):
            return True
        else:
            pantalla.red_text("Formato inválido. Solo se permiten letras.")
            return False
    return True