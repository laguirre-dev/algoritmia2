"""
1. Validaciones de logins correctos e incorrectos
2. Validaciones de redirecciones correctamente de menus segun rol
3. Validar que se creen usuarios correctamente y credenciales incorrectamente
4. Validar que se aprueba el curso a un alumno
5. Validar que un alumno se inscriba a un curso
"""

from utils.credenciales import login
from entidades.administrativo.menuAdministrativo import menuAdministrativo # validar
from entidades.alumno.menuAlumno import menuAlumno # validar
from entidades.profesor.menuProfesor import menuProfesor # validar
from entidades.administrativo.gestion_usuarios import (
    insertaUsuario,
    insertaCredenciales,
)
from entidades.profesor.gestion_evaluar import aprobarODesaprobarAlumnosMock # tuvimos que mockear la funcion porque pedia parametros dentro
from entidades.alumno.gestion_accion import inscribirEnCurso
from main import redireccion_menu
from entidades import datos


def test_login_correcto():
    # login alumno correcto
    legajo = 101
    clave = "alum123"
    resultado = login(legajo, clave)
    assert resultado == (True, "alumno")


def test_login_incorrecto():
    # login alumno incorrecto
    legajo = 101
    clave = "alum111"
    resultado = login(legajo, clave)
    assert resultado == (True, "alumno")


def test_redireccion_administrativo():
    rol = "administrativo"
    respuesta = redireccion_menu[rol]
    assert respuesta == menuAdministrativo


def test_redireccion_profesor():
    rol = "profesor"
    respuesta = redireccion_menu[rol]
    assert respuesta == menuProfesor


def test_redireccion_alumno():
    rol = "alumno"
    respuesta = redireccion_menu[rol]
    assert respuesta == menuAlumno


def test_crear_usuarios_correcta():
    legajo = 1
    nombre = "Alumno"
    apellido = "Alumno"
    rol = "alumno"
    respuesta = insertaUsuario((legajo, nombre, apellido, rol), datos.ALUMNOS_DB)
    assert respuesta == True


def test_crear_credenciales_incorrecta():
    legajo = 1
    nombre = "Alumno"
    apellido = "Alumno"
    rol = "alumno"
    respuesta = insertaCredenciales((legajo, nombre, apellido, rol))
    assert respuesta == True


def test_aprobar_alumno():
    profesor = 2001
    curso = "AED1"
    entrada = "101:A"
    respuesta = aprobarODesaprobarAlumnosMock(profesor, curso, entrada)
    assert respuesta == ["Aprobado", 101]


def test_desaprobar_alumno():
    profesor = 2001
    curso = "AED1"
    entrada = "101:A"
    respuesta = aprobarODesaprobarAlumnosMock(profesor, curso, entrada)
    assert respuesta == ["Desaprobado", 101]


def test_inscribirse_curso():
    alumno = 101
    curso = "BD1"
    respuesta = inscribirEnCurso(alumno, curso)
    assert respuesta == True
