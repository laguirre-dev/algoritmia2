# datos.py
# Base de datos en memoria para el Sistema de Gestión de Alumnos, para que en un futuro tengamos que solo modificar estos datos.

# Lista de alumnos
ALUMNOS_DB = []

# Lista de profesores
PROFESORES_DB = []

# Lista de cursos/materias
CURSOS_DB = [
    {"id": "AED1", "nombre": "Algoritmos y Estructuras de Datos I", "profesor": None, "aula": None, "alumnos": []},
    {"id": "PROG2", "nombre": "Programación II", "profesor": None, "aula": None, "alumnos": []}
]

# Cuotas pendientes
CUOTAS_PENDIENTES = []

# Credenciales para login
CREDENCIALES = [
    {"legajo": 9999, "clave": "uade123", "rol": "administrativo"},
    {"legajo": 2001, "clave": "prof123", "rol": "profesor"},
    {"legajo": 101, "clave": "alum123", "rol": "alumno"}
]