"""
El objetivo del modulo es centralizar las funciones reutilizables para usarlas en cualquier parte de las funciones
1. Buscar alumno
2. Buscar profesor
3. Buscar materia
4. Buscar pagos

Las funciones deben devolver el contenido de la entidad filtrada: Por ej, detalles del alumno, materia, pago (alumno, monto, vencimiento, etc)
"""

import entidades.datos as datos


def buscar_alumno():
    print("En desarrollo...") #
    return

def buscarAlumnoPorLegajo(legajo):
    return next((alumno for alumno in datos.ALUMNOS_DB if alumno.get("legajo") == legajo), None)

def buscar_profesor():
    print("En desarrollo...")
    return

def buscar_materia():
    print("En desarrollo...")
    return

def buscarCursoPorId(idCurso):
    return next((curso for curso in datos.CURSOS_DB if curso.get("id") == idCurso), None)

def buscar_pagos():
    print("En desarrollo...")
    return
