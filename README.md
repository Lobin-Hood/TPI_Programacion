# Sistema de Gestión de Países 🌎

**Trabajo Práctico Integrador (TPI) - Programación 1**

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar una base de datos de países.
El sistema lee y escribe información desde un archivo CSV, garantizando la persistencia de los datos entre diferentes sesiones de uso.

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Librerías:** Únicamente funciones integradas de Python (sin dependencias externas).
*   **Estructuras de datos:** Listas y Diccionarios (`list[dict]`).
*   **Persistencia:** Manejo de archivos de texto plano (.csv) mediante lectura/escritura nativa.

## 📁 Estructura del Proyecto

El repositorio consta de los siguientes archivos principales:
*   `scripts/main.py`: Contiene el código fuente completo del programa, modularizado en funciones con sus respectivos *Type Hints* y *Docstrings*.
*   `data/paises.csv`: Archivo de base de datos que almacena los registros iniciales y los cambios realizados por el usuario.

## 💻 Instalación y Uso

1.  Clonar este repositorio en tu máquina local:
```bash
    git clone https://github.com/Lobin-Hood/TPI_Programacion
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

## 🚀 Diagrama de Flujo (con ejemplos de uso)

1. [Inicio]
2. [Cargar Datos] (Lista de Diccionarios desde el CSV)
3. [Mostrar Menú Principal]
4. [Ingresar Opción]
5. [¿Opción Válida?]
   - NO: Mostrar error y volver a (3).
   - SÍ: Avanzar a (6).
6. [Evaluar Opción 1 a 8]
   - Opciones 1 a 7: Ejecutar función correspondiente y volver a (3).
   - Opción 8: Sobrescribir archivo CSV y avanzar a (7).
7. [Fin]

<br>
<p><img src="https://drive.google.com/uc?export=view&id=111ZuiOqAabB1-2ObFZ0FoZ-LLi1DJ33X" width="300"/>
<br>Menú Principal</p>
<p><img src="https://drive.google.com/uc?export=view&id=1hFVEJx0PHTU1G2nne93pNvgMu4BzUQ2D" width="300"/>
<br>Ver todos los países: Imprime una tabla formateada con la información completa del dataset.</p>
<p><img src="https://drive.google.com/uc?export=view&id=1JdU6VA0sTE39pVzTNXbR-hX25Me8CYpH" width="300"/>
<br>Buscar país: Permite realizar búsquedas por nombre (coincidencia exacta o parcial).</p>
<p><img src="https://drive.google.com/uc?export=view&id=1FcSBarVOK6SSoxyQBA1_KpkzBcUgZNtr" width="300"/>
<br>Actualizar datos: Modifica la población y/o superficie de un país existente en el registro.</p>
<p><img src="https://drive.google.com/uc?export=view&id=1r8PR2CrDg2ztvpLnpSDzl3qDBFzVoeLc" width="300"/>
<br>Agregar país: Incorpora nuevos registros (validando que no existan duplicados y que los datos numéricos sean mayores a cero).</p>
<p><img src="https://drive.google.com/uc?export=view&id=1uBwATEgXOJdv22l7D2zahinCgydOYnid" width="300"/>
<br>Filtrar países: Aplica filtros específicos por Continente, Rango de Población o Rango de Superficie.</p>
<p><img src="https://drive.google.com/uc?export=view&id=1vLDLVYNCjPbYSR1cXZtPp5O_zFuWHsIt" width="300"/>
<br>Ordenar países: Organiza la lista de forma ascendente o descendente según nombre, población, superficie o continente.</p>
<p><img src="https://drive.google.com/uc?export=view&id=1Fr2NKNKAJ_x1NAIVMy-1sf5Xr0qyOp0q" width="300"/>
<br>Estadísticas: Muestra promedios globales, los países con mayor/menor población y el conteo total de países por continente.</p>
<p><img src="https://drive.google.com/uc?export=view&id=1P_wc1NEoXxFbDlTAFVaJOyv7sZsjwceh" width="300"/>
<br>Mensaje de Salida</p>

## 👨‍💻 Autor

*   **LOBO, Pablo (M26 C1-24, R-Villa María)**

## 🔗 Links Útiles
* [Documentación en PDF](https://drive.google.com/file/d/1RXM6RWEWXStXB094moeBWPjBmnXchSCm)
* [Video Explicativo](https://drive.google.com/file/d/1su4veKbbsOHClB14P6T4hWD12n0OWzIB)

---
*Proyecto desarrollado para la cátedra de Programación 1 - [1° cuatrimestre 2026].*
