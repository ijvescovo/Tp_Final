import sqlite3

def mostrar_menu():
    """Muestra el menú principal."""
    print("\nMenú para la Gestión de Productos:")
    print("1. Registro: Alta de productos nuevos.")
    print("2. Búsqueda: Consulta de datos de un producto específico.")
    print("3. Actualización: Modificar solo la cantidad de un producto.")
    print("4. Eliminación: Dar de baja productos.")
    print("5. Listado: Listado completo de los productos en la base de datos.")
    print("6. Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.")
    print("7. Salir.")

def obtener_precio():
    """Obtiene y valida el precio del producto."""
    while True:
        try:
            precio = float(input("Precio del producto:"))
            if precio > 0:
                return precio
            else:
                print("Entrada inválida. Debe ingresar un número decimal mayor a 0.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un valor numérico decimal mayor a 0.")

def obtener_cantidad(nombre):
    """Obtiene y valida la cantidad en stock del producto."""
    while True:
        try:
            cantidad = int(input(f"Cantidad en stock de {nombre}:"))
            if cantidad >= 0:
                return cantidad
            else:
                print("Entrada inválida. El stock no puede ser negativo.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un valor numérico entero.")

def registrar_producto(conexion):
    """Registra un nuevo producto."""
    print("\n--- Registro de Producto Nuevo ---")
    nombre = input("Nombre del producto:").strip()
    descripcion = input("Descripción del producto:").strip()
    precio = obtener_precio()
    cantidad = obtener_cantidad(nombre)
    categoria = input("Categoría del producto:").strip()

    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (Nombre, Descripción, Cantidad, Precio, Categoria) VALUES (?, ?, ?, ?, ?)",
                       (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print("Producto registrado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al registrar el producto: {e}");
