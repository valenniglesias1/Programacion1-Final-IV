"""
Módulo para el manejo de archivos y persistencia de datos.

Se encarga de leer y escribir los datos del sistema de stock
en formato JSON, manejando errores de archivos y validando
la integridad de los datos.
"""

import json
import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from models import Product

# Cargar variables de entorno
load_dotenv()


def obtener_ruta_archivo() -> str:
    """
    Obtiene la ruta del archivo de datos desde variables de entorno.

    Returns:
        str: Ruta del archivo de datos. Por defecto 'datos_stock.json'.
    """
    return os.getenv("DATA_FILE_PATH", "datos_stock.json")


def cargar_productos() -> List[Product]:
    """
    Carga los productos desde el archivo JSON.

    Si el archivo no existe, retorna una lista vacía.
    Si el archivo está corrupto o tiene formato inválido,
    muestra un error y retorna una lista vacía.

    Returns:
        List[Product]: Lista de productos cargados desde el archivo.

    Example:
        >>> productos = cargar_productos()
        >>> print(f"Se cargaron {len(productos)} productos")
    """
    ruta_archivo = obtener_ruta_archivo()
    productos = []

    try:
        if not os.path.exists(ruta_archivo):
            return productos

        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            print(f"Error: El archivo {ruta_archivo} no tiene formato válido.")
            return productos

        for item in datos:
            try:
                producto = Product.from_dict(item)
                productos.append(producto)
            except (KeyError, ValueError, TypeError) as e:
                print(f"Error al cargar producto: {e}")
                continue

    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta_archivo} está corrupto o "
              f"tiene formato JSON inválido.")
    except PermissionError:
        print(f"Error: No se tienen permisos para leer el archivo "
              f"{ruta_archivo}.")
    except Exception as e:
        print(f"Error inesperado al cargar productos: {e}")

    return productos


def guardar_productos(productos: List[Product]) -> bool:
    """
    Guarda la lista de productos en el archivo JSON.

    Args:
        productos (List[Product]): Lista de productos a guardar.

    Returns:
        bool: True si se guardó correctamente, False en caso contrario.

    Example:
        >>> productos = [Product("PROD001", "Laptop", "Electrónica", 50000, 10)]
        >>> guardar_productos(productos)
        True
    """
    ruta_archivo = obtener_ruta_archivo()

    try:
        datos = [producto.to_dict() for producto in productos]

        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)

        return True

    except PermissionError:
        print(f"Error: No se tienen permisos para escribir en el archivo "
              f"{ruta_archivo}.")
        return False
    except Exception as e:
        print(f"Error inesperado al guardar productos: {e}")
        return False

