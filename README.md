# Sistema de Gestión de Stock de Productos

## Idea del Proyecto

Este proyecto fue desarrollado como trabajo final de la materia Programación 1. El objetivo principal fue aplicar los conceptos vistos durante la cursada, priorizando la claridad del código, la organización y las buenas prácticas.

### Qué es el sistema?

El sistema es una aplicación de línea de comandos (CLI) que permite gestionar un inventario de productos de forma eficiente, manteniendo un registro persistente de todos los productos, sus características y cantidades disponibles.

### Qué problema resuelve?

El sistema resuelve la necesidad de tener un control centralizado y organizado del inventario de productos, permitiendo:

- Registrar nuevos productos con sus características
- Modificar información de productos existentes
- Eliminar productos del inventario
- Consultar y buscar productos de manera rápida
- Mantener la información persistente entre sesiones

### Funcionalidades del Sistema

El sistema debe implementar las siguientes funcionalidades obligatorias:

1. **Alta de productos**: Agregar nuevos productos al inventario con código único, nombre, categoría, precio y cantidad inicial
2. **Modificación de productos**: Actualizar precio y/o cantidad de productos existentes
3. **Baja de productos**: Eliminar productos del inventario
4. **Listado de productos**: Visualizar todos los productos registrados en formato tabular
5. **Búsqueda de productos**: Buscar productos por código o por nombre (búsqueda parcial)

### Enfoque del Proyecto

- Esté bien programado
- Esté bien organizado
- Esté bien documentado
- Aplique las buenas prácticas vistas en clase
- Sea modular y mantenible
- Siga los estándares de la industria

Este proyecto se realiza como **Trabajo Final de Programación 1 – Infraestructura**.

---

## Objetivo del README

Este README funciona como:

- **Documento de definición del proyecto**: Define qué se debe construir
- **Documento de reglas técnicas**: Establece qué tecnologías y herramientas usar
- **Guía obligatoria para desarrollar**: Proporciona instrucciones claras para el desarrollo

---

## Lenguaje y Entorno

### Obligatorio

- **Python 3.10 o superior**
- **Ejecución por consola** (interfaz de línea de comandos)
- **Uso de entorno virtual (venv)** (ver sección correspondiente)
- **Control de versiones con GitHub**

### No Permitido

- Interfaces gráficas (Tkinter, PyQT, etc.)
- Frameworks web (Flask, Django, FastAPI, etc.)
- Bases de datos (MySQL, SQLite, PostgreSQL, etc.)
- Código sin modularizar
- Código sin documentar

---

## Estructura Obligatoria del Proyecto

El proyecto debe seguir esta estructura de archivos y carpetas:

```
sistema_stock/

main.py                  # Punto de entrada del programa
stock_manager.py         # Lógica del sistema de stock (módulo propio)
file_handler.py          # Manejo de archivos (módulo propio)
models.py                # Modelos de datos (módulo propio)
requirements.txt         # Dependencias externas
README.md                # Este archivo
.gitignore              # Ignora venv y archivos innecesarios
venv/                   # Entorno virtual (NO se sube al repositorio)
```

### Descripción de Archivos

- **`main.py`**: Contiene el punto de entrada del programa, el menú principal y la interfaz de usuario
- **`stock_manager.py`**: Contiene la lógica de negocio del sistema (operaciones CRUD, validaciones)
- **`file_handler.py`**: Maneja la lectura y escritura de archivos (persistencia de datos)
- **`models.py`**: Define las estructuras de datos utilizadas (clases, dataclasses)
- **`requirements.txt`**: Lista todas las dependencias externas del proyecto
- **`.gitignore`**: Especifica qué archivos y carpetas no deben subirse al repositorio
- **`README.md`**: Documentación completa del proyecto

---

## Funcionalidades Obligatorias

### Gestión de Productos

Cada producto debe tener los siguientes atributos:

- **Código único**: Identificador único del producto (string)
- **Nombre**: Nombre descriptivo del producto (string)
- **Categoría**: Categoría a la que pertenece el producto (string)
- **Precio**: Precio unitario del producto (float, mayor a 0)
- **Cantidad en stock**: Cantidad disponible del producto (int, mayor o igual a 0)

### Operaciones CRUD

El sistema debe implementar:

- **Crear (Agregar)**: Agregar un nuevo producto al inventario
- **Leer (Consultar)**: Listar todos los productos y buscar productos específicos
- **Actualizar (Modificar)**: Modificar precio y/o cantidad de productos existentes
- **Eliminar**: Eliminar productos del inventario

### Persistencia de Datos

- **Guardar datos**: Los datos deben guardarse en archivo (JSON o CSV)
- **Cargar datos**: Los datos deben cargarse automáticamente al iniciar el programa
- **Guardado automático**: Los cambios deben persistirse después de cada operación

---

## Uso de Módulos


El proyecto debe utilizar **al menos 2 módulos externos** instalados mediante `pip`. Estos módulos deben estar listados en `requirements.txt` y ser utilizados de manera significativa en el código.

**Ejemplos**:
- `rich`: Para mejorar la presentación en consola (tablas, colores, menús)
- `python-dotenv`: Para manejo de variables de entorno y configuración
- `colorama`: Para colores en la consola
- `tabulate`: Para formateo de tablas

**Requisitos**:
- Todas las dependencias deben estar listadas en `requirements.txt`
- Deben instalarse mediante `pip install -r requirements.txt`
- Deben ejecutarse dentro del entorno virtual (`venv`)

### Módulos Propios

El proyecto debe incluir **módulos creados por el desarrollador**, separados del `main.py`, con responsabilidades claras y bien definidas.

**Requisitos**:
- Separados del `main.py`
- Con responsabilidad clara y única
- Con docstring de módulo (ver sección Docstrings)
- Bien organizados y reutilizables

**Ejemplos**:
- `stock_manager.py` → Lógica del sistema de stock
- `file_handler.py` → Lectura/escritura de archivos
- `models.py` → Estructuras de datos

---

## Zen de Python


### Se eligio "Simple es mejor que complejo"

El código debe ser simple y directo. Evitar soluciones innecesariamente complicadas cuando existe una solución más simple y clara.

**Ejemplo de aplicación**:
- Usar estructuras de datos simples (listas, diccionarios)
- Evitar abstracciones innecesarias
- Preferir funciones pequeñas y específicas sobre funciones grandes y complejas

### Explícito es mejor que implícito

El código debe ser claro y explícito. Evitar comportamientos ocultos o implícitos que dificulten la comprensión.

**Ejemplo de aplicación**:
- Usar nombres de variables y funciones descriptivos
- Validar explícitamente los datos de entrada
- Manejar errores de forma explícita con `try/except`
- Documentar claramente qué hace cada función

### La legibilidad es importante

El código debe ser fácil de leer y entender. La legibilidad facilita el mantenimiento y la colaboración.

**Ejemplo de aplicación**:
- Seguir PEP 8 (ver sección correspondiente)
- Usar comentarios cuando sea necesario
- Organizar el código de forma lógica
- Separar responsabilidades en módulos distintos

### Los errores nunca deberían pasar silenciosamente

Todos los errores deben ser manejados y reportados de manera adecuada. No se permite que el programa finalice abruptamente sin informar al usuario.

**Ejemplo de aplicación**:
- Usar `try/except` para manejar errores
- Mostrar mensajes de error claros al usuario
- Validar datos de entrada antes de procesarlos
- Manejar errores de archivos (archivo inexistente, datos corruptos, etc.)

---

## Entorno Virtual (venv) – Obligatorio

### Qué es un entorno virtual?

Un entorno virtual es un directorio aislado que contiene una instalación de Python y sus paquetes. Permite tener diferentes versiones de paquetes para diferentes proyectos sin conflictos.

### Por qué es obligatorio?

- **Aislamiento**: Evita conflictos entre dependencias de diferentes proyectos
- **Reproducibilidad**: Permite que otros desarrolladores instalen exactamente las mismas versiones
- **Limpieza**: Mantiene el sistema Python global limpio
- **Buenas prácticas**: Es el estándar en el desarrollo de Python

### Crear el Entorno Virtual

```bash
python -m venv venv
```

Este comando crea una carpeta `venv/` con el entorno virtual.

### Activar el Entorno Virtual

**Windows**:
```bash
venv\Scripts\activate
```

**Linux / macOS**:
```bash
source venv/bin/activate
```

Una vez activado, verás `(venv)` al inicio de la línea de comandos.

### Instalar Dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

### Desactivar el Entorno Virtual

```bash
deactivate
```

### IMPORTANTE: La carpeta `venv/` NO debe subirse al repositorio

La carpeta `venv/` debe estar incluida en el `.gitignore` para evitar subirla al repositorio. Cada desarrollador debe crear su propio entorno virtual.

---

## Estilo de Código – PEP 8

El código debe cumplir estrictamente con las convenciones de estilo **PEP 8** (Python Enhancement Proposal 8).

### Indentación

- **4 espacios** por nivel de indentación
- **NO usar tabs**
- Usar espacios de forma consistente

### Longitud de Líneas

- **Máximo 79 caracteres** por línea
- Si una línea es muy larga, dividirla en múltiples líneas usando paréntesis o backslash

### Nombres

- **Variables y funciones**: `snake_case` (minúsculas con guiones bajos)
  - Ejemplo: `agregar_producto`, `codigo_producto`
- **Constantes**: `UPPER_CASE` (mayúsculas con guiones bajos)
  - Ejemplo: `MAX_PRODUCTOS`, `RUTA_ARCHIVO`
- **Clases**: `PascalCase` (primera letra de cada palabra en mayúscula)
  - Ejemplo: `StockManager`, `Product`

### Importaciones

- Las importaciones deben estar ordenadas:
  1. Librerías estándar de Python
  2. Librerías de terceros
  3. Módulos locales
- Un espacio en blanco entre cada grupo
- Una importación por línea

**Ejemplo**:
```python
import json
import os
from typing import List, Dict

from dotenv import load_dotenv
from rich.console import Console

from models import Product
from file_handler import cargar_productos
```

### Espacios en Blanco

- Dos líneas en blanco antes de definiciones de clases o funciones de nivel superior
- Una línea en blanco antes de definiciones de métodos dentro de una clase
- Usar espacios alrededor de operadores, pero no dentro de paréntesis

### Código Legible

- **NO se permite**: Código "apretado" sin espacios
- **NO se permite**: Variables con nombres sin sentido (`x`, `temp`, `data`)
- **NO se permite**: Funciones excesivamente largas (más de 50 líneas)

---

## Documentación del Código – PEP 257

### Docstrings – Obligatorio

Todas las funciones y módulos deben tener **docstrings** siguiendo el estándar **PEP 257**.

### Docstrings de Módulos

Cada módulo debe comenzar con un docstring que explique:
- Qué hace el módulo
- Su propósito principal
- Qué funciones o clases contiene

**Ejemplo**:
```python
"""
Módulo de gestión de stock de productos.

Contiene la lógica de negocio para el sistema de gestión de stock,
incluyendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
y validaciones de datos.
"""
```

### Docstrings de Funciones

Cada función debe tener un docstring que explique:

1. **Qué hace la función**: Descripción breve y clara
2. **Parámetros**: Tipo y descripción de cada parámetro
3. **Valor de retorno**: Tipo y descripción del valor retornado
4. **Posibles excepciones**: Qué excepciones puede lanzar

**Formato obligatorio**:
```python
def agregar_producto(codigo: str, nombre: str, precio: float, 
                     cantidad: int) -> Tuple[bool, str]:
    """
    Agrega un nuevo producto al sistema de stock.

    Valida todos los campos antes de agregar y verifica que
    el código no exista previamente.

    Args:
        codigo (str): Código único del producto.
        nombre (str): Nombre del producto.
        precio (float): Precio unitario.
        cantidad (int): Cantidad inicial en stock.

    Returns:
        Tuple[bool, str]: Tupla con (éxito, mensaje).
            éxito: True si se agregó correctamente, False en caso contrario.
            mensaje: Mensaje descriptivo del resultado.

    Raises:
        ValueError: Si algún parámetro es inválido.
    """
```

### No se permite código sin docstrings

Todas las funciones, clases y módulos deben estar documentados.

---


### Validaciones de Entrada de Datos

El programa debe validar:

- Que **ningún campo obligatorio esté vacío**
- Que los valores ingresados respeten el **tipo de dato esperado**
- Que los valores numéricos sean **válidos y coherentes**

#### Código de Producto

- Debe ser **único** (no puede haber dos productos con el mismo código)
- Debe ser **string**
- No puede estar vacío
- No se permite duplicación de códigos

#### Nombre del Producto

- Debe ser **string**
- No puede estar vacío
- No debe contener solo números

#### Categoría

- Debe ser **string**
- No puede estar vacía

#### Precio

- Debe ser **numérico** (float)
- Debe ser **mayor a 0**
- No se permiten valores negativos
- No se permiten valores cero

#### Cantidad en Stock

- Debe ser **entero** (int)
- Debe ser **mayor o igual a 0**
- No se permiten valores negativos

### Validaciones de Operaciones

#### Alta de Producto

- Verificar que el código no exista previamente
- Validar todos los campos antes de guardar
- Mostrar mensaje de error claro si la validación falla

#### Modificación de Producto

- Verificar que el producto exista
- Validar los nuevos valores antes de actualizar
- No permitir valores inválidos

#### Eliminación de Producto

- Verificar que el producto exista antes de eliminar
- Confirmar la acción (opcional pero recomendado)

#### Búsqueda

- Verificar que el criterio de búsqueda no esté vacío
- Manejar correctamente búsquedas sin resultados

### Validaciones de Archivos

- Verificar si el archivo de datos existe
- Si no existe, crear uno vacío automáticamente
- Manejar errores de lectura/escritura con `try/except`
- Evitar que el programa se detenga por archivos corruptos
- Mostrar mensajes de error claros al usuario

### Manejo de Errores (Obligatorio)

El sistema debe:

- Usar `try/except` en todas las operaciones críticas:
  - Lectura/escritura de archivos
  - Conversión de tipos (string a int/float)
  - Operaciones de validación
- Mostrar mensajes de error claros al usuario
- **NO finalizar abruptamente** ante errores no controlados
- Evitar errores silenciosos (todos los errores deben ser reportados)

### Relación con el Zen de Python

Estas validaciones aplican los principios:

- **Explícito es mejor que implícito**: Validar explícitamente todos los datos
- **Los errores nunca deberían pasar silenciosamente**: Manejar y reportar todos los errores
- **La legibilidad es importante**: Mensajes de error claros y comprensibles

Todas las validaciones deben estar separadas en funciones claras y reutilizables.

---




## Instrucciones de Uso

### 1. Clonar o Descargar el Proyecto

```bash
git clone <url-del-repositorio>
cd sistema_stock
```

### 2. Crear el Entorno Virtual

```bash
python -m venv venv
```

### 3. Activar el Entorno Virtual

**Windows**:
```bash
venv\Scripts\activate
```

**Linux / macOS**:
```bash
source venv/bin/activate
```

### 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el Programa

```bash
python main.py
```

### 6. Usar el Sistema

Seguir las instrucciones del menú para:
- Agregar productos
- Modificar productos
- Eliminar productos
- Listar productos
- Buscar productos


---

## Referencias

- [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 – Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Desarrollado como Trabajo Final de Programación 1 – Infraestructura IT (ISTEA)**

