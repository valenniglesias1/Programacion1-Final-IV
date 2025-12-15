"""
Módulo de modelos de datos para el sistema de gestión de stock.

Define las estructuras de datos utilizadas en el sistema,
especialmente el modelo Product que representa un producto
en el inventario.
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Product:
    """
    Representa un producto en el sistema de stock.

    Attributes:
        codigo (str): Código único identificador del producto.
        nombre (str): Nombre descriptivo del producto.
        categoria (str): Categoría a la que pertenece el producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad disponible en stock.

    Example:
        >>> producto = Product("PROD001", "Laptop", "Electrónica", 50000.0, 10)
        >>> print(producto.nombre)
        Laptop
    """

    codigo: str
    nombre: str
    categoria: str
    precio: float
    cantidad: int

    def to_dict(self) -> Dict[str, Any]:
        """
        Convierte el producto a un diccionario.

        Returns:
            Dict[str, Any]: Diccionario con los datos del producto.
        """
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Product':
        """
        Crea un Product desde un diccionario.

        Args:
            data (Dict[str, Any]): Diccionario con los datos del producto.

        Returns:
            Product: Instancia de Product creada desde el diccionario.

        Raises:
            KeyError: Si faltan campos requeridos en el diccionario.
        """
        return cls(
            codigo=data["codigo"],
            nombre=data["nombre"],
            categoria=data["categoria"],
            precio=float(data["precio"]),
            cantidad=int(data["cantidad"])
        )

