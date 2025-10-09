import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")