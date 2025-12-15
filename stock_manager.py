"""
Módulo de gestión de stock de productos.

Contiene la lógica de negocio para el sistema de gestión de stock,
incluyendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
y validaciones de datos.
"""

from typing import List, Optional, Tuple
from models import Product
from file_handler import cargar_productos, guardar_productos


class StockManager:
    """
    Gestor del sistema de stock de productos.

    Maneja todas las operaciones relacionadas con el inventario:
    agregar, modificar, eliminar, listar y buscar productos.
    """

    def __init__(self):
        """
        Inicializa el gestor de stock cargando productos desde archivo.
        """
        self.productos: List[Product] = cargar_productos()

    def _validar_codigo(self, codigo: str) -> bool:
        """
        Valida que el código sea único y no esté vacío.

        Args:
            codigo (str): Código a validar.

        Returns:
            bool: True si el código es válido, False en caso contrario.
        """
        if not codigo or not codigo.strip():
            return False
        return True

    def _codigo_existe(self, codigo: str) -> bool:
        """
        Verifica si un código ya existe en el sistema.

        Args:
            codigo (str): Código a verificar.

        Returns:
            bool: True si el código existe, False en caso contrario.
        """
        return any(p.codigo == codigo for p in self.productos)

    def _validar_nombre(self, nombre: str) -> bool:
        """
        Valida que el nombre no esté vacío y no sea solo números.

        Args:
            nombre (str): Nombre a validar.

        Returns:
            bool: True si el nombre es válido, False en caso contrario.
        """
        if not nombre or not nombre.strip():
            return False
        if nombre.strip().isdigit():
            return False
        return True

    def _validar_categoria(self, categoria: str) -> bool:
        """
        Valida que la categoría no esté vacía.

        Args:
            categoria (str): Categoría a validar.

        Returns:
            bool: True si la categoría es válida, False en caso contrario.
        """
        return bool(categoria and categoria.strip())

    def _validar_precio(self, precio: float) -> bool:
        """
        Valida que el precio sea mayor a 0.

        Args:
            precio (float): Precio a validar.

        Returns:
            bool: True si el precio es válido, False en caso contrario.
        """
        return precio > 0

    def _validar_cantidad(self, cantidad: int) -> bool:
        """
        Valida que la cantidad sea mayor o igual a 0.

        Args:
            cantidad (int): Cantidad a validar.

        Returns:
            bool: True si la cantidad es válida, False en caso contrario.
        """
        return cantidad >= 0

    def agregar_producto(self, codigo: str, nombre: str, categoria: str,
                        precio: float, cantidad: int) -> Tuple[bool, str]:
        """
        Agrega un nuevo producto al sistema.

        Valida todos los campos antes de agregar y verifica que
        el código no exista previamente.

        Args:
            codigo (str): Código único del producto.
            nombre (str): Nombre del producto.
            categoria (str): Categoría del producto.
            precio (float): Precio unitario.
            cantidad (int): Cantidad inicial en stock.

        Returns:
            tuple[bool, str]: Tupla con (éxito, mensaje).
                éxito: True si se agregó correctamente, False en caso contrario.
                mensaje: Mensaje descriptivo del resultado.
        """
        if not self._validar_codigo(codigo):
            return False, "El código no puede estar vacío."

        if self._codigo_existe(codigo):
            return False, f"El código '{codigo}' ya existe en el sistema."

        if not self._validar_nombre(nombre):
            return False, "El nombre no puede estar vacío o ser solo números."

        if not self._validar_categoria(categoria):
            return False, "La categoría no puede estar vacía."

        if not self._validar_precio(precio):
            return False, "El precio debe ser mayor a 0."

        if not self._validar_cantidad(cantidad):
            return False, "La cantidad debe ser mayor o igual a 0."

        nuevo_producto = Product(codigo, nombre, categoria, precio, cantidad)
        self.productos.append(nuevo_producto)

        if guardar_productos(self.productos):
            return True, f"Producto '{nombre}' agregado correctamente."
        else:
            self.productos.remove(nuevo_producto)
            return False, "Error al guardar el producto en el archivo."

    def modificar_producto(self, codigo: str, precio: Optional[float] = None,
                          cantidad: Optional[int] = None) -> Tuple[bool, str]:
        """
        Modifica el precio y/o cantidad de un producto existente.

        Args:
            codigo (str): Código del producto a modificar.
            precio (Optional[float]): Nuevo precio (None para no modificar).
            cantidad (Optional[int]): Nueva cantidad (None para no modificar).

        Returns:
            tuple[bool, str]: Tupla con (éxito, mensaje).
                éxito: True si se modificó correctamente, False en caso contrario.
                mensaje: Mensaje descriptivo del resultado.
        """
        producto = self.buscar_por_codigo(codigo)
        if not producto:
            return False, f"Producto con código '{codigo}' no encontrado."

        cambios = False

        if precio is not None:
            if not self._validar_precio(precio):
                return False, "El precio debe ser mayor a 0."
            producto.precio = precio
            cambios = True

        if cantidad is not None:
            if not self._validar_cantidad(cantidad):
                return False, "La cantidad debe ser mayor o igual a 0."
            producto.cantidad = cantidad
            cambios = True

        if not cambios:
            return False, "No se especificaron cambios a realizar."

        if guardar_productos(self.productos):
            return True, f"Producto '{producto.nombre}' modificado correctamente."
        else:
            return False, "Error al guardar los cambios en el archivo."

    def eliminar_producto(self, codigo: str) -> Tuple[bool, str]:
        """
        Elimina un producto del sistema.

        Args:
            codigo (str): Código del producto a eliminar.

        Returns:
            tuple[bool, str]: Tupla con (éxito, mensaje).
                éxito: True si se eliminó correctamente, False en caso contrario.
                mensaje: Mensaje descriptivo del resultado.
        """
        producto = self.buscar_por_codigo(codigo)
        if not producto:
            return False, f"Producto con código '{codigo}' no encontrado."

        nombre = producto.nombre
        self.productos.remove(producto)

        if guardar_productos(self.productos):
            return True, f"Producto '{nombre}' eliminado correctamente."
        else:
            self.productos.append(producto)
            return False, "Error al guardar los cambios en el archivo."

    def listar_productos(self) -> List[Product]:
        """
        Retorna la lista completa de productos.

        Returns:
            List[Product]: Lista de todos los productos en el sistema.
        """
        return self.productos.copy()

    def buscar_por_codigo(self, codigo: str) -> Optional[Product]:
        """
        Busca un producto por su código.

        Args:
            codigo (str): Código del producto a buscar.

        Returns:
            Optional[Product]: Producto encontrado o None si no existe.
        """
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def buscar_por_nombre(self, nombre: str) -> List[Product]:
        """
        Busca productos cuyo nombre contenga el texto especificado.

        La búsqueda es case-insensitive (no distingue mayúsculas/minúsculas).

        Args:
            nombre (str): Texto a buscar en los nombres.

        Returns:
            List[Product]: Lista de productos que coinciden con la búsqueda.
        """
        if not nombre or not nombre.strip():
            return []

        nombre_lower = nombre.lower().strip()
        resultados = []

        for producto in self.productos:
            if nombre_lower in producto.nombre.lower():
                resultados.append(producto)

        return resultados

