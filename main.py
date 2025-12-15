"""
Sistema de Gestión de Stock de Productos.

Punto de entrada principal del programa. Proporciona una interfaz
de línea de comandos (CLI) para gestionar el inventario de productos.

Este módulo implementa el menú principal y coordina las operaciones
del sistema utilizando los módulos stock_manager, file_handler y models.
"""

import sys
from typing import List
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from stock_manager import StockManager
from models import Product

console = Console()


def mostrar_menu() -> None:
    """
    Muestra el menú principal del sistema en la consola.
    """
    menu_text = """
[bold cyan]╔════════════════════════════════════════╗[/bold cyan]
[bold cyan]║  SISTEMA DE GESTIÓN DE STOCK          ║[/bold cyan]
[bold cyan]╚════════════════════════════════════════╝[/bold cyan]

[bold]1.[/bold] Agregar producto
[bold]2.[/bold] Modificar producto
[bold]3.[/bold] Eliminar producto
[bold]4.[/bold] Listar todos los productos
[bold]5.[/bold] Buscar producto por código
[bold]6.[/bold] Buscar producto por nombre
[bold]0.[/bold] Salir
"""
    console.print(Panel(menu_text, title="[bold green]Menú Principal[/bold green]",
                       border_style="green"))


def mostrar_tabla_productos(productos: List[Product]) -> None:
    """
    Muestra una tabla formateada con los productos usando Rich.

    Args:
        productos (list[Product]): Lista de productos a mostrar.
    """
    if not productos:
        console.print("[yellow]No hay productos para mostrar.[/yellow]")
        return

    tabla = Table(title="[bold cyan]Productos en Stock[/bold cyan]",
                  show_header=True, header_style="bold magenta")

    tabla.add_column("Código", style="cyan", no_wrap=True)
    tabla.add_column("Nombre", style="green")
    tabla.add_column("Categoría", style="yellow")
    tabla.add_column("Precio", style="blue", justify="right")
    tabla.add_column("Cantidad", style="red", justify="right")

    for producto in productos:
        tabla.add_row(
            producto.codigo,
            producto.nombre,
            producto.categoria,
            f"${producto.precio:.2f}",
            str(producto.cantidad)
        )

    console.print(tabla)


def obtener_float(mensaje: str) -> float:
    """
    Solicita al usuario un número decimal válido.

    Args:
        mensaje (str): Mensaje a mostrar al usuario.

    Returns:
        float: Número decimal ingresado por el usuario.

    Raises:
        KeyboardInterrupt: Si el usuario cancela la operación.
    """
    while True:
        try:
            valor = Prompt.ask(mensaje)
            return float(valor)
        except ValueError:
            console.print("[red]Error: Debe ingresar un número válido.[/red]")
        except KeyboardInterrupt:
            console.print("\n[yellow]Operación cancelada.[/yellow]")
            raise


def obtener_int(mensaje: str) -> int:
    """
    Solicita al usuario un número entero válido.

    Args:
        mensaje (str): Mensaje a mostrar al usuario.

    Returns:
        int: Número entero ingresado por el usuario.

    Raises:
        KeyboardInterrupt: Si el usuario cancela la operación.
    """
    while True:
        try:
            valor = Prompt.ask(mensaje)
            return int(valor)
        except ValueError:
            console.print("[red]Error: Debe ingresar un número entero.[/red]")
        except KeyboardInterrupt:
            console.print("\n[yellow]Operación cancelada.[/yellow]")
            raise


def opcion_agregar_producto(manager: StockManager) -> None:
    """
    Maneja la opción de agregar un nuevo producto.

    Args:
        manager (StockManager): Instancia del gestor de stock.
    """
    console.print("\n[bold cyan]═══════════════════════════════════[/bold cyan]")
    console.print("[bold cyan]Agregar Nuevo Producto[/bold cyan]")
    console.print("[bold cyan]═══════════════════════════════════[/bold cyan]\n")

    try:
        codigo = Prompt.ask("[bold]Código del producto[/bold]")
        nombre = Prompt.ask("[bold]Nombre del producto[/bold]")
        categoria = Prompt.ask("[bold]Categoría[/bold]")
        precio = obtener_float("[bold]Precio[/bold]")
        cantidad = obtener_int("[bold]Cantidad en stock[/bold]")

        exito, mensaje = manager.agregar_producto(
            codigo, nombre, categoria, precio, cantidad)

        if exito:
            console.print(f"[green]✓ {mensaje}[/green]")
        else:
            console.print(f"[red]✗ {mensaje}[/red]")

    except KeyboardInterrupt:
        console.print("\n[yellow]Operación cancelada.[/yellow]")


def opcion_modificar_producto(manager: StockManager) -> None:
    """
    Maneja la opción de modificar un producto existente.

    Args:
        manager (StockManager): Instancia del gestor de stock.
    """
    console.print("\n[bold cyan]═══════════════════════════════════[/bold cyan]")
    console.print("[bold cyan]Modificar Producto[/bold cyan]")
    console.print("[bold cyan]═══════════════════════════════════[/bold cyan]\n")

    try:
        codigo = Prompt.ask("[bold]Código del producto a modificar[/bold]")
        producto = manager.buscar_por_codigo(codigo)

        if not producto:
            console.print(f"[red]✗ Producto con código '{codigo}' no encontrado.[/red]")
            return

        console.print(f"\n[bold]Producto actual:[/bold] {producto.nombre}")
        console.print(f"Precio actual: ${producto.precio:.2f}")
        console.print(f"Cantidad actual: {producto.cantidad}\n")

        modificar_precio = Confirm.ask("[bold]¿Modificar precio?[/bold]")
        modificar_cantidad = Confirm.ask("[bold]¿Modificar cantidad?[/bold]")

        nuevo_precio = None
        nueva_cantidad = None

        if modificar_precio:
            nuevo_precio = obtener_float("[bold]Nuevo precio[/bold]")

        if modificar_cantidad:
            nueva_cantidad = obtener_int("[bold]Nueva cantidad[/bold]")

        exito, mensaje = manager.modificar_producto(
            codigo, nuevo_precio, nueva_cantidad)

        if exito:
            console.print(f"[green]✓ {mensaje}[/green]")
        else:
            console.print(f"[red]✗ {mensaje}[/red]")

    except KeyboardInterrupt:
        console.print("\n[yellow]Operación cancelada.[/yellow]")


def opcion_eliminar_producto(manager: StockManager) -> None:
    """
    Maneja la opción de eliminar un producto.

    Args:
        manager (StockManager): Instancia del gestor de stock.
    """
    console.print("\n[bold cyan]═══════════════════════════════════[/bold cyan]")
    console.print("[bold cyan]Eliminar Producto[/bold cyan]")
    console.print("[bold cyan]═══════════════════════════════════[/bold cyan]\n")

    try:
        codigo = Prompt.ask("[bold]Código del producto a eliminar[/bold]")
        producto = manager.buscar_por_codigo(codigo)

        if not producto:
            console.print(f"[red]✗ Producto con código '{codigo}' no encontrado.[/red]")
            return

        console.print(f"\n[bold]Producto a eliminar:[/bold] {producto.nombre}")
        console.print(f"Código: {producto.codigo}")
        console.print(f"Categoría: {producto.categoria}\n")

        confirmar = Confirm.ask("[bold red]¿Está seguro de eliminar este producto?[/bold red]")

        if confirmar:
            exito, mensaje = manager.eliminar_producto(codigo)
            if exito:
                console.print(f"[green]✓ {mensaje}[/green]")
            else:
                console.print(f"[red]✗ {mensaje}[/red]")
        else:
            console.print("[yellow]Operación cancelada.[/yellow]")

    except KeyboardInterrupt:
        console.print("\n[yellow]Operación cancelada.[/yellow]")


def opcion_listar_productos(manager: StockManager) -> None:
    """
    Maneja la opción de listar todos los productos.

    Args:
        manager (StockManager): Instancia del gestor de stock.
    """
    console.print("\n[bold cyan]═══════════════════════════════════[/bold cyan]")
    console.print("[bold cyan]Listado de Productos[/bold cyan]")
    console.print("[bold cyan]═══════════════════════════════════[/bold cyan]\n")

    productos = manager.listar_productos()
    mostrar_tabla_productos(productos)


def opcion_buscar_por_codigo(manager: StockManager) -> None:
    """
    Maneja la opción de buscar un producto por código.

    Args:
        manager (StockManager): Instancia del gestor de stock.
    """
    console.print("\n[bold cyan]═══════════════════════════════════[/bold cyan]")
    console.print("[bold cyan]Buscar Producto por Código[/bold cyan]")
    console.print("[bold cyan]═══════════════════════════════════[/bold cyan]\n")

    try:
        codigo = Prompt.ask("[bold]Ingrese el código del producto[/bold]")
        producto = manager.buscar_por_codigo(codigo)

        if producto:
            mostrar_tabla_productos([producto])
        else:
            console.print(f"[yellow]No se encontró producto con código '{codigo}'.[/yellow]")

    except KeyboardInterrupt:
        console.print("\n[yellow]Operación cancelada.[/yellow]")


def opcion_buscar_por_nombre(manager: StockManager) -> None:
    """
    Maneja la opción de buscar productos por nombre.

    Args:
        manager (StockManager): Instancia del gestor de stock.
    """
    console.print("\n[bold cyan]═══════════════════════════════════[/bold cyan]")
    console.print("[bold cyan]Buscar Producto por Nombre[/bold cyan]")
    console.print("[bold cyan]═══════════════════════════════════[/bold cyan]\n")

    try:
        nombre = Prompt.ask("[bold]Ingrese el nombre (o parte del nombre)[/bold]")
        productos = manager.buscar_por_nombre(nombre)

        if productos:
            console.print(f"\n[green]Se encontraron {len(productos)} producto(s):[/green]\n")
            mostrar_tabla_productos(productos)
        else:
            console.print(f"[yellow]No se encontraron productos con nombre '{nombre}'.[/yellow]")

    except KeyboardInterrupt:
        console.print("\n[yellow]Operación cancelada.[/yellow]")


def main() -> None:
    """
    Función principal del programa.

    Inicializa el sistema, muestra el menú y maneja las opciones
    seleccionadas por el usuario hasta que se elija salir.
    """
    console.print("\n[bold green]Iniciando Sistema de Gestión de Stock...[/bold green]\n")

    manager = StockManager()
    productos_cargados = len(manager.listar_productos())

    if productos_cargados > 0:
        console.print(f"[green]✓ Se cargaron {productos_cargados} producto(s) desde el archivo.[/green]\n")
    else:
        console.print("[yellow]No se encontraron productos. El sistema está vacío.[/yellow]\n")

    while True:
        try:
            mostrar_menu()
            opcion = Prompt.ask("\n[bold]Seleccione una opción[/bold]", default="0")

            if opcion == "1":
                opcion_agregar_producto(manager)
            elif opcion == "2":
                opcion_modificar_producto(manager)
            elif opcion == "3":
                opcion_eliminar_producto(manager)
            elif opcion == "4":
                opcion_listar_productos(manager)
            elif opcion == "5":
                opcion_buscar_por_codigo(manager)
            elif opcion == "6":
                opcion_buscar_por_nombre(manager)
            elif opcion == "0":
                console.print("\n[bold green]¡Gracias por usar el Sistema de Gestión de Stock![/bold green]\n")
                sys.exit(0)
            else:
                console.print("[red]✗ Opción inválida. Por favor, seleccione una opción válida.[/red]")

            if opcion != "0":
                Prompt.ask("\n[dim]Presione Enter para continuar...[/dim]")

        except KeyboardInterrupt:
            console.print("\n\n[yellow]Operación cancelada por el usuario.[/yellow]")
            console.print("[bold green]¡Gracias por usar el Sistema de Gestión de Stock![/bold green]\n")
            sys.exit(0)
        except Exception as e:
            console.print(f"\n[red]Error inesperado: {e}[/red]")
            console.print("[yellow]El sistema continuará funcionando.[/yellow]\n")


if __name__ == "__main__":
    main()

