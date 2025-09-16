# datos.py
# Base de datos en memoria para el Sistema de Gestión de Alumnos, para que en un futuro tengamos que solo modificar estos datos.

# Lista de alumnos
ALUMNOS_DB = []

# Lista de profesores
PROFESORES_DB = []

CURSOS_DB = [
    {"id": "AED1", "nombre": "Algoritmos y Estructuras de Datos I", "profesor": None, "aula": None, "alumnos": []},
    {"id": "PROG2", "nombre": "Programación II", "profesor": None, "aula": None, "alumnos": []}
]

# Cuotas pendientes

CUOTAS_PENDIENTES = []

# Credenciales para login
CREDENCIALES = [
    {"Legajo": 9999, "Password": "uade123", "Rol": "admin"},
    {"Legajo": 2001, "Password": "prof123", "Rol": "profesor"},
    {"Legajo": 101, "Password": "alum123", "Rol": "alumno"}
]
