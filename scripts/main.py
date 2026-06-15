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
            entrada = input(mensaje.strip())
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
        print(f"\n{'Nombre':<20} | {'Población':<15} | {'Superficie (km²)':<18} | {'Continente':<15}")
        print("-" * 75)
        for pais in datos:
            print(f"{pais['nombre']:<20} | {pais['poblacion']:<15} | {pais['superficie']:<18} | {pais['continente']:<15}")
        print("-" * 75)

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
        print("8. Salir")
        print("="*40)
        try:
            opcion_menu = int(input("Seleccione una opción: "))
            if opcion_menu == 1: imprimir_tabla(datos)
            elif opcion_menu == 2: pass # buscar_pais(datos)
            elif opcion_menu == 3: pass # actualizar_pais(datos)
            elif opcion_menu == 4: pass # agregar_pais(datos)
            elif opcion_menu == 5: pass # filtrar_paises(datos)
            elif opcion_menu == 6: pass # ordenar_paises(datos)
            elif opcion_menu == 7: pass # mostrar_estadisticas(datos)
            elif opcion_menu == 8: print("Finalizando la ejecución del sistema.")
            else: raise ValueError
        except ValueError:
            print("Error: Entrada no válida. Debe ingresar un número entero entre 1 y 8.")

if __name__ == "__main__":
    main()
