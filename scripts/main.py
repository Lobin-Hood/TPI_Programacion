# Nombre del archivo donde se encuentran los datos
ruta_csv = "data/paises.csv"
respaldo_csv = "data/BackUp.csv"

def pedir_texto(mensaje: str) -> str:
    """
    Solicita al usuario un ingreso de texto
    y valida que no se esté vacío.

    Args:
        mensaje (str): texto para mostrar al usuario.
    Returns:
        string con entrada del usuario.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        print("Error: este campo no puede quedar vacío.")

def pedir_entero(mensaje: str) -> int:
    """
    Solicita al usuario un ingreso de número entero
    y valida que ingrese un número entero válido y mayor o igual a cero.

    Args:
        mensaje (str): texto para mostrar al usuario.
    Returns:
        número entero mayor o igual a cero.
    """
    while True:
        try:
            entrada = input(mensaje).strip()
            if not entrada:
                print("Error: este campo no puede quedar vacío.")
                continue
            if not entrada.isdigit():
                print("Debe ingresar un número entero válido (sin puntos ni comas).")
                continue
            entrada = int(entrada)
            if entrada > 0:
                return entrada
            print("Error: el número debe ser mayor a cero.")
        except Exception as e:
            raise Exception(f"Error al convertir a entero: {e}")

def cargar_datos(ruta_archivo: str) -> list[dict]:
    """
    Lee el archivo CSV y retorna una lista de diccionarios.
    
    Args:
        ruta_archivo (str): string con la ruta al archivo.
    Returns:
        lista de diccionarios con la información del archivo.
    """
    datos = []
    try:
        with open(ruta_archivo, mode = "r", encoding = "utf-8") as archivo:
            campos = archivo.readline().split(",")
            for linea in archivo:
                valores = linea.strip().split(",")
                if len(valores) != len(campos):
                    print(f"Línea con formato incorrecto: {linea}")
                    continue
                datos.append({
                    campos[0].strip(): valores[0].strip(),
                    campos[1].strip(): int(valores[1].strip()),
                    campos[2].strip(): int(valores[2].strip()),
                    campos[3].strip(): valores[3].strip()
                })
    except FileNotFoundError:
        print(f"No se encontró '{ruta_archivo}'.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
    return datos

def guardar_datos(ruta_archivo: str, datos: list[dict]) -> None:
    """
    Guarda la lista de diccionarios en el archivo CSV.
    
    Args:
        ruta_archivo (str): string con la ruta al archivo.
        datos (list[dict]): lista de diccionarios con la información.
    """
    try:
        with open(ruta_archivo, mode = 'w', encoding = 'utf-8', newline = '') as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")
            for pais in datos:
                archivo.write(",".join(map(str,(pais.values()))) + "\n")
    except FileNotFoundError:
        print(f"No se encontró '{ruta_archivo}'.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

def imprimir_tabla(datos: list[dict]) -> None:
    """
    Imprime una lista de países en formato tabular por consola.
    
    Args:
        datos (list[dict]): lista de diccionarios con la información.
    """
    if not datos:
        print("No hay datos para mostrar.")
    else:    
        print(f"\n{'Nombre':<20} | {'Población':<20} | {'Superficie (km²)':<20} | {'Continente':<20}")
        print("-" * 80)
        for pais in datos:
            print(f"{pais['nombre']:<20} | {format(pais['poblacion'],","):<20} | {format(pais['superficie'],","):<20} | {pais['continente']:<20}")
        print("-" * 80)

def buscar_pais(datos: list[dict]) -> None:
    """
    Busca países por coincidencia exacta o parcial en el nombre.
    
    Args:
        datos (list[dict]): lista de diccionarios con la información.
    """
    print("\n--- BUSCAR PAÍS ---")
    busqueda = pedir_texto("Ingrese el nombre a buscar (puede ser parcial): ").lower()
    resultados = [pais for pais in datos if busqueda in pais['nombre'].lower()]
    if resultados:
        print("\nResultados de la búsqueda:")
        imprimir_tabla(resultados)
    else:
        print("No se encontraron países que coincidan con la búsqueda.")

def actualizar_pais(datos: list[dict]) -> None:
    """
    Actualiza la población y superficie de un país existente,
    y lo guarda en el csv.
    
    Args:
        datos (list[dict]): lista de diccionarios con la información.
    """
    print("\n--- ACTUALIZAR PAÍS ---")
    nombre = pedir_texto("Ingrese el nombre exacto del país a actualizar: ")
    for pais in datos:
        if pais['nombre'].lower() == nombre.lower():
            print(f"\nPaís encontrado: {pais['nombre']} | Continente: {pais['continente']}")
            print(f"Población actual: {pais['poblacion']} | Superficie actual: {pais['superficie']} km²")
            pais['poblacion'] = pedir_entero("Ingrese la NUEVA población: ")
            pais['superficie'] = pedir_entero("Ingrese la NUEVA superficie en km²: ")
            print("Datos actualizados exitosamente.")
            return
    print("Error: No se encontró ningún país con ese nombre exacto.")

def agregar_pais(datos: list[dict]) -> None:
    """
    Agrega un nuevo país validando las entradas,
    y lo guarda en el csv.
    
    Args:
        datos (list[dict]): lista de diccionarios con la información.
    """
    print("\n--- AGREGAR NUEVO PAÍS ---")
    nombre = pedir_texto("Ingrese el nombre del país: ")
    # Verificamos si ya existe, para evitar duplicados exactos
    if any(pais['nombre'].lower() == nombre.lower() for pais in datos):
        print("Error: el país ya existe en el registro.")
    else:
        poblacion = pedir_entero("Ingrese la población: ")
        superficie = pedir_entero("Ingrese la superficie en km²: ")
        continente = pedir_texto("Ingrese el continente: ")
        datos.append({
            'nombre': nombre,
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente
        })
        print("País agregado exitosamente.")

def filtrar_paises(datos: list[dict]) -> None:
    """
    Aplica filtros según el continente, población o superficie.
    Luego, muestra la tabla con los resultados.

    Args:
        datos (list[dict]): lista de diccionarios con la información.
    """
    print("\n--- FILTRAR PAÍSES ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    try:
        resultados = []
        opcion_submenu = int(input("Seleccione el tipo de filtro (1-3): ").strip())
        if opcion_submenu == 1:
            continente = pedir_texto("Ingrese el continente a filtrar: ").lower()
            resultados = [pais for pais in datos if continente in pais['continente'].lower()]
        elif opcion_submenu == 2:
            print("\nDefina el rango de Población")
            poblacion_minima = pedir_entero("Población mínima: ")
            poblacion_maxima = pedir_entero("Población máxima: ")
            resultados = [pais for pais in datos if poblacion_minima <= pais['poblacion'] <= poblacion_maxima]
        elif opcion_submenu == 3:
            print("\nDefina el rango de Superficie")
            superficie_minima = pedir_entero("Superficie mínima: ")
            superficie_maxima = pedir_entero("Superficie máxima: ")
            resultados = [pais for pais in datos if superficie_minima <= pais['superficie'] <= superficie_maxima]
        else: raise ValueError
    except ValueError:
        print("Error: Entrada no válida. Debe ingresar un número entero entre 1 y 3.")
        return
    if resultados: imprimir_tabla(resultados)
    else: print("No se encontraron países que cumplan con los criterios especificados.")

def ordenar_paises(datos: list[dict]) -> None:
    """
    Ordena según el nombre, población, superficie o continente.
    Luego, muestra la tabla con los resultados.

    Args:
        datos (list[dict]): lista de diccionarios con la información.
    """
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    print("4. Por Continente")
    try:
        opcion_submenu = int(input("Seleccione el tipo de filtro (1-4): ").strip())
        if opcion_submenu not in range(1, 5): raise ValueError
        orden = input("¿Desea orden ascendente o descendente? (a/d): ").strip().lower()
        while orden not in ['a', 'd']:
            orden = input("Entrada inválida. Ingrese 'a' para ascendente o 'd' para descendente: ").strip().lower()
        criterio = list(datos[0].keys())[opcion_submenu - 1]
        datos_ordenados = sorted(datos, key = lambda x: x[criterio], reverse = (orden == 'd'))
    except ValueError:
        print("Error: Entrada no válida. Debe ingresar un número entero entre 1 y 4.")
        return
    imprimir_tabla(datos_ordenados)

def mostrar_estadisticas(datos: list[dict]) -> None:
    """
    Calcula y muestra estadísticas generales del dataset.
    
    Args:
        datos (list[dict]): lista de diccionarios con la información.
    """
    print("\n--- ESTADÍSTICAS ---")
    if not datos:
        print("Error: No hay datos suficientes para calcular estadísticas.")
        return
    # País con mayor y menor población
    pais_mayor_poblacion = max(datos, key = lambda x: x['poblacion'])
    pais_menor_poblacion = min(datos, key = lambda x: x['poblacion'])
    print(f"País con MAYOR población: {pais_mayor_poblacion['nombre']} ({format(pais_mayor_poblacion['poblacion'], ",")} habitantes)")
    print(f"País con MENOR población: {pais_menor_poblacion['nombre']} ({format(pais_menor_poblacion['poblacion'], ",")} habitantes)")
    # Promedios
    total_poblacion = sum(pais['poblacion'] for pais in datos)
    total_superficie = sum(pais['superficie'] for pais in datos)
    total_paises = len(datos)
    print(f"\nPromedio de población global: {total_poblacion / total_paises:,.2f} habitantes")
    print(f"Promedio de superficie global: {total_superficie / total_paises:,.2f} km²")
    # Cantidad de países por continente
    continentes = list()
    for pais in datos: continentes.append(pais['continente'])
    print("\nCantidad de países registrados por continente:")
    for continente in set(continentes): print(f" - {continente}: {continentes.count(continente)} países")

def main():
    # Cargamos los datos al abrir el programa
    datos = cargar_datos(ruta_csv)
    # Mostramos el menú principal
    opcion_menu = 0
    while opcion_menu != 8:
        print("\n" + "="*40)
        print("--- SISTEMA DE GESTIÓN DE PAÍSES ---")
        print("="*40)
        print("1. Ver todos los países")
        print("2. Buscar un país por nombre")
        print("3. Actualizar datos de un país")
        print("4. Agregar un nuevo país")
        print("5. Filtrar países")
        print("6. Ordenar países")
        print("7. Mostrar estadísticas")
        print("8. Guardar y Salir")
        print("="*40)
        try:
            opcion_menu = int(input("Seleccione una opción: "))
            if opcion_menu == 1: imprimir_tabla(datos)
            elif opcion_menu == 2: buscar_pais(datos)
            elif opcion_menu == 3: actualizar_pais(datos)
            elif opcion_menu == 4: agregar_pais(datos)
            elif opcion_menu == 5: filtrar_paises(datos)
            elif opcion_menu == 6: ordenar_paises(datos)
            elif opcion_menu == 7: mostrar_estadisticas(datos)
            elif opcion_menu == 8: guardar_datos(ruta_csv, datos)
            else: raise ValueError
        except ValueError:
            print("Error: Entrada no válida. Debe ingresar un número entero entre 1 y 8.")
    print("Finalizando ejecución del sistema.")

if __name__ == "__main__":
    main()
