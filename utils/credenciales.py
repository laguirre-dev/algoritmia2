def crear_clave(legajo, nombre, apellido):
    parte1 = str(legajo)
    parte2 = nombre[0].upper()
    parte3 = apellido.lower()
    return parte1 + parte2 + parte3


def imprimir_credenciales(legajo, clave):
    print("\n#####################")
    print("Legajo: ", legajo)
    print("Clave: ", clave)
    print("#####################\n")
