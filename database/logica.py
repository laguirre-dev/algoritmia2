import os

def convertirListaTupla(lista):
    for alumno in lista:
        cursos_convertidos_tuplas = []
        for curso in alumno["cursos"]:
            cursos_convertidos_tuplas.append(tuple(curso))
        alumno["cursos"] = cursos_convertidos_tuplas
    return lista
