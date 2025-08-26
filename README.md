# Sistema de Gestión de Alumnos

### 1. **Introducción**

El presente documento define el alcance del proyecto “Sistema de Gestión de Alumnos”, desarrollado en Python como trabajo práctico obligatorio de la materia *Algoritmos y Estructuras de Datos I*.
El sistema será una aplicación de consola (interfaz por terminal), orientada a la gestión básica de cursos, alumnos, profesores y administrativos.

---

### 2. **Objetivo General**

Diseñar e implementar un sistema sencillo de gestión académica que permita a los usuarios interactuar con la información de alumnos, cursos y pagos, garantizando modularidad, facilidad de uso y cumplimiento con los contenidos de la materia (listas, diccionarios, manejo de archivos, pruebas unitarias, excepciones, etc.).

---

### 3. **Objetivos Específicos**

* Implementar un sistema multi-rol (Profesor, Alumno, Administrativo).
* Practicar el uso de estructuras de datos (listas, diccionarios, tuplas, conjuntos).
* Implementar control de errores y validaciones.
* Desarrollar persistencia básica mediante archivos JSON.
* Modularizar el código en diferentes archivos para mejorar la legibilidad.
* Aplicar pruebas unitarias a funciones clave.

---

### 4. **Alcance Funcional**

#### **Roles y Funciones**

* **Alumno**

  * Inscribirse en un curso.
  * Ver cursos disponibles.
  * Consultar pagos adeudados.
  * Visualizar estado de aprobación (aprobado / desaprobado).
* **Profesor**

  * Visualizar cursos y aulas asignadas.
  * Aprobar o desaprobar alumnos.
* **Administrativo**

  * Asignar cursos y aulas a profesores.
  * Aprobar pagos de alumnos.

#### **Restricciones**

* No se gestionarán notas numéricas (solo aprobado / desaprobado).
* No se implementará interfaz gráfica, solo terminal.
* No se contemplan múltiples sedes ni jerarquías avanzadas.

---

### 5. **Entregables**

1. **Documento de Alcance y Repositorio Inicial (Semana 4).**

   * Documento de alcance.
   * Repositorio GitHub creado con estructura inicial.

2. **Modularización del código (Semana 5).**

   * Separación en módulos: `main.py`, `alumno.py`, `profesor.py`, `administrativo.py`.

3. **Primer Entregable Formal (Semana 7 – 40%).**

   * Funcionalidades básicas de alta de alumnos, inscripción a cursos, y asignación de profesor.

4. **Segundo Entregable Formal (Semana 16 – 80%).**

   * Persistencia en archivos JSON.
   * Manejo de excepciones.
   * Pruebas unitarias básicas.

5. **Entrega Final (Semana 18 – 100%).**

   * Sistema completo funcionando.
   * Documentación final en el repositorio.

---

### 6. **Tecnologías y Herramientas**

* **Lenguaje:** Python
* **Gestión de versiones:** Git + GitHub
* **Paradigma:** Programación estructurada / modular
* **Almacenamiento:** Archivos planos (TXT / JSON)
* **Librerias:** os (operaciones del sistema), json (persistencia de datos), unittest (pruebas unitarias en funciones), datetime (control de fechas), re (validaciones)

### 7. Conclusión

El “Sistema de Gestión de Alumnos” es un proyecto que busca integrar los conceptos fundamentales de la materia en una aplicación práctica y concreta. Se trabajará con estructuras de datos, modularización, manejo de archivos y pruebas, respetando los hitos del cronograma académico.

El sistema permitirá gestionar alumnos, cursos y profesores desde la terminal. De este modo, se logra un equilibrio entre simplicidad y desafío.

Con este proyecto se espera que se pueda practicar programación estructurada, desarrollar buenas prácticas de organización del código, y familiarizarse con herramientas y metodologías ágiles, obteniendo un resultado concreto y funcional al finalizar el proyecto.
