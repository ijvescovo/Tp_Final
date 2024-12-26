import sqlite3
import os

def conectar_db():
    """Conecta a la base de datos o la crea si no existe."""
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    nombre_bbdd = os.path.join(directorio_actual, "db", "inventario.db")
    try:
        conexion = sqlite3.connect(nombre_bbdd)
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def inicializar_bbdd(conexion):
    """Crea la tabla productos si no existe."""
    try:
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Codigo TEXT UNIQUE,
                Nombre TEXT NOT NULL,
                Descripcion TEXT,
                Cantidad INTEGER NOT NULL CHECK(Cantidad >= 0),
                Precio REAL NOT NULL CHECK(Precio > 0),
                Categoria TEXT
            )
        ''')
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")

def registrar_producto(conexion, nombre, descripcion, cantidad, precio, categoria):
    """Registra un nuevo producto."""
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (Nombre, Descripcion, Cantidad, Precio, Categoria) VALUES (?, ?, ?, ?, ?)",
                       (nombre, descripcion, cantidad, precio, categoria))
        id_producto = cursor.lastrowid
        codigo = f"PROD{id_producto}"
        cursor.execute("UPDATE productos SET Codigo = ? WHERE id = ?", (codigo, id_producto))
        conexion.commit()
        return codigo
    except sqlite3.IntegrityError:
        print("Error. No se pudo registrar el producto (probablemente código duplicado).")
        return None
    except sqlite3.Error as e:
        print(f"Error al registrar producto: {e}")
        return None

def buscar_producto(conexion, codigo):
    """Busca un producto por código."""
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE Codigo = ?", (codigo,))
        producto = cursor.fetchone()
        return producto
    except sqlite3.Error as e:
        print(f"Error al buscar producto: {e}")
        return None

def actualizar_producto(conexion, codigo, nueva_cantidad):
    """Actualiza solo la cantidad de un producto."""
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET Cantidad = ? WHERE Codigo = ?", (nueva_cantidad, codigo))
        conexion.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error al actualizar producto: {e}")
        return False

def eliminar_producto(conexion, codigo):
    """Elimina un producto por código."""
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE Codigo = ?", (codigo,))
        conexion.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error al eliminar producto: {e}")
        return False

def listar_productos(conexion):
    """Lista todos los productos."""
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        return productos
    except sqlite3.Error as e:
        print(f"Error al listar productos: {e}")
        return None
