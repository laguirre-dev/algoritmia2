import os
from colorama import init, Fore, Style

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
    
init(autoreset=True)

def header(titulo):
    print(Fore.GREEN + "=" * 50)
    print(Style.BRIGHT + Fore.WHITE + titulo.center(50))
    print(Fore.GREEN + "=" * 50)