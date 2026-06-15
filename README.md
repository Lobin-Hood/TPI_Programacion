# Sistema de Gestión de Países 🌎

**Trabajo Práctico Integrador (TPI) - Programación 1**

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar una base de datos de países.
El sistema lee y escribe información desde un archivo CSV, garantizando la persistencia de los datos entre diferentes sesiones de uso.

## 🚀 Características Principales

El programa cuenta con un menú interactivo que ofrece las siguientes funcionalidades:
*   **Ver todos los países:** Imprime una tabla formateada con la información completa del dataset.
*   **Buscar país:** Permite realizar búsquedas por nombre (coincidencia exacta o parcial).
*   **Actualizar datos:** Modifica la población y/o superficie de un país existente en el registro.
*   **Agregar país:** Incorpora nuevos registros (validando que no existan duplicados y que los datos numéricos sean mayores a cero).
*   **Filtrar países:** Aplica filtros específicos por Continente, Rango de Población o Rango de Superficie.
*   **Ordenar países:** Organiza la lista de forma ascendente o descendente según nombre, población, superficie o continente.
*   **Estadísticas:** Muestra promedios globales, los países con mayor/menor población y el conteo total de países por continente.

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Librerías:** Únicamente funciones integradas de Python (sin dependencias externas).
*   **Estructuras de datos:** Listas y Diccionarios (`list[dict]`).
*   **Persistencia:** Manejo de archivos de texto plano (.csv) mediante lectura/escritura nativa.

## 📁 Estructura del Proyecto

El repositorio consta de los siguientes archivos principales:
*   `main.py`: Contiene el código fuente completo del programa, modularizado en funciones con sus respectivos *Type Hints* y *Docstrings*.
*   `data/paises.csv`: Archivo de base de datos que almacena los registros iniciales y los cambios realizados por el usuario.

## 💻 Instalación y Uso

1.  Clonar este repositorio en tu máquina local:
```bash
    git clone [https://github.com/Lobin-Hood/TPI_Programacion.git](https://github.com/Lobin-Hood/TPI_Programacion.git)
    ```
2.  Navegar a la carpeta del proyecto:
```bash
    cd TPI_Programacion
    ```
3.  Ejecutar el script principal desde la terminal:
```bash
    python main.py
    ```

> **Nota:** No es necesario instalar librerías adicionales ni entornos virtuales, ya que el proyecto utiliza exclusivamente la biblioteca estándar de Python.

## 👨‍💻 Autor

*   **LOBO, Pablo (M26 C1-24, R-Villa María)**

---
*Proyecto desarrollado para la cátedra de Programación 1 - [1° cuatrimestre 2026].*