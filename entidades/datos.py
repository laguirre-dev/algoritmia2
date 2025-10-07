# Base de datos en memoria para el Sistema de Gestión de Alumnos

# Lista de alumnos
# Cada alumno tiene: legajo, nombre, apellido, cursos = [(idCurso, estado)]
ALUMNOS_DB = [
    {"legajo": 101, "nombre": "Alumno", "apellido": "Alumno", "cursos": [("AED1", "Desaprobado")]},
    {"legajo": 102, "nombre": "Dario", "apellido": "Andreatini", "cursos": [("AED1", "Desaprobado"), ("PROG2", "Desaprobado")]},
    {"legajo": 103, "nombre": "Nacho", "apellido": "Bonavoglia", "cursos": [("PROG2", "Desaprobado"), ("BD1", "Desaprobado")]},
    {"legajo": 104, "nombre": "Luciano", "apellido": "Aguirre", "cursos": [("BD1", "Desaprobado"), ("PY1", "Desaprobado")]},
    {"legajo": 105, "nombre": "Federico", "apellido": "Kerekes", "cursos": [("MAT1", "Desaprobado")]},
    {"legajo": 106, "nombre": "Sofia", "apellido": "Perez", "cursos": [("FIS1", "Desaprobado"), ("EST1", "Desaprobado")]},
    {"legajo": 107, "nombre": "Lucas", "apellido": "Gomez", "cursos": [("ING1", "Desaprobado"), ("RED1", "Desaprobado")]}
]

# Lista de profesores
# Cada profesor tiene: legajo, nombre, apellido, materias = [idCurso]
PROFESORES_DB = [
    {"legajo": 2001, "nombre": "Juan", "apellido": "Lopez", "materias": ["AED1", "PROG2"]},
    {"legajo": 2002, "nombre": "Maria", "apellido": "Torres", "materias": ["BD1", "PY1"]},
    {"legajo": 2003, "nombre": "Carlos", "apellido": "Fernandez", "materias": ["MAT1", "FIS1", "EST1", "ING1", "RED1", "SO1"]}
]

# Lista de cursos/materias
# Cada curso tiene: id, nombre, profesor (legajo), aula, alumnos (legajos)
CURSOS_DB = [
    {"id": "AED1", "nombre": "Algoritmos y Estructuras de Datos I", "profesor": 2001, "aula": "Aula 101", "alumnos": [101, 102]},
    {"id": "PROG2", "nombre": "Programación II", "profesor": 2001, "aula": "Aula 202", "alumnos": [102, 103]},
    {"id": "BD1", "nombre": "Bases de Datos I", "profesor": 2002, "aula": "Aula 303", "alumnos": [103, 104]},
    {"id": "PY1", "nombre": "Python Inicial", "profesor": 2002, "aula": "Aula 404", "alumnos": [104]},
    {"id": "MAT1", "nombre": "Matemática Discreta", "profesor": 2003, "aula": "Aula 105", "alumnos": [105]},
    {"id": "FIS1", "nombre": "Física I", "profesor": 2003, "aula": "Aula 106", "alumnos": [106]},
    {"id": "EST1", "nombre": "Estadística I", "profesor": 2003, "aula": "Aula 107", "alumnos": [106]},
    {"id": "ING1", "nombre": "Inglés Técnico I", "profesor": 2003, "aula": "Aula 108", "alumnos": [107]},
    {"id": "RED1", "nombre": "Redes de Computadoras I", "profesor": 2003, "aula": "Aula 109", "alumnos": [107]},
    {"id": "SO1", "nombre": "Sistemas Operativos I", "profesor": 2003, "aula": "Aula 110", "alumnos": []}
]

# Cuotas pendientes
CUOTAS_PENDIENTES = [
    {"cuota_nro": 1, "legajo": 102},
    {"cuota_nro": 2, "legajo": 102},
    {"cuota_nro": 1, "legajo": 103},
    {"cuota_nro": 1, "legajo": 104},
    {"cuota_nro": 3, "legajo": 105}
]

# Credenciales para login
CREDENCIALES = [
    {"legajo": 9999, "clave": "uade123", "rol": "administrativo"},
    {"legajo": 2001, "clave": "prof123", "rol": "profesor"},
    {"legajo": 2002, "clave": "maria2002", "rol": "profesor"},
    {"legajo": 2003, "clave": "carlos2003", "rol": "profesor"},
    {"legajo": 101, "clave": "alum123", "rol": "alumno"},
    {"legajo": 102, "clave": "dario102", "rol": "alumno"},
    {"legajo": 103, "clave": "nacho103", "rol": "alumno"},
    {"legajo": 104, "clave": "luciano104", "rol": "alumno"},
    {"legajo": 105, "clave": "federico105", "rol": "alumno"},
    {"legajo": 106, "clave": "sofia106", "rol": "alumno"},
    {"legajo": 107, "clave": "lucas107", "rol": "alumno"}
]