# datos.py
# Base de datos en memoria para el Sistema de Gestión de Alumnos, para que en un futuro tengamos que solo modificar estos datos.
"""
Estructura de cada entidad:
alumno: legajo, nombre, apellido, activo, pagos_pendientes, materias => alumno -> pago -> pago_pendiente -> administrativo
profesor: legajo, nombre, apellido, activo, materias_asignadas => profesor -> nota -> alumno.materias
materia: id, nombre, profesor, aula, alumnos
pagos_pendientes: alumno, materia, monto
credenciales: legajo, clave, rol
"""


# Lista de alumnos
ALUMNOS_DB = [
    {
        "legajo": 101,
        "nombre": "Alumno",
        "apellido": "Alumno",
        "activo": True,
        "pagos_pendientes": [
            {"materia": "Algoritmia 2", "monto": 8500, "estado": "pendiente"}
        ],
        "materias": [{"nombre": "Algoritmia 2", "nota_final": 7}],
    }
]

# Lista de profesores
PROFESORES_DB = [
    {"legajo": 2001, "nombre": "Profesor", "apellido": "Profesor", "materias": []}
]

# Lista de cursos/materias
CURSOS_DB = [
    {
        "id": "AED1",
        "nombre": "Algoritmos y Estructuras de Datos I",
        "profesor": None,
        "aula": None,
        "alumnos": [],
    },
    {
        "id": "PROG2",
        "nombre": "Programación II",
        "profesor": None,
        "aula": None,
        "alumnos": [],
    },
]

# Pagos pendientes
PAGOS_PENDIENTES = []

# Credenciales para login
CREDENCIALES = [
    {"legajo": 9999, "clave": "uade123", "rol": "administrativo"},
    {"legajo": 2001, "clave": "prof123", "rol": "profesor"},
    {"legajo": 101, "clave": "alum123", "rol": "alumno"},
]
