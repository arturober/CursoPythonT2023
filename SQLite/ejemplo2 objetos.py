from dataclasses import dataclass
import sqlite3

@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    
def product_factory(cursor, row):
    return Producto(row[0], row[1], row[2])

conexion = sqlite3.connect("SQLite/productos.sqlite")
conexion.row_factory = product_factory # A partir de ahora devuelve objetos de Producto
cursor = conexion.cursor()

def crear_tabla():
    tabla_productos = """
    DROP TABLE IF EXISTS productos;

    CREATE TABLE productos(
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        precio REAL
    )
    """

    cursor.executescript(
        tabla_productos
    )  # Permite ejecutar más de 1 sentencia SQL seguida


def crear_producto(nombre, precio):
    cursor.execute(
        "INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio)
    )
    conexion.commit()
    print(cursor.lastrowid)  # Última id autogenerada


# crear_producto("Silla", 23)


def mod_producto(id, nombre, precio):
    cursor.execute(
        "UPDATE productos SET nombre = ?, precio = ? WHERE id = ?", (nombre, precio, id)
    )
    conexion.commit()
    print(f"{cursor.rowcount} registros actualizados")


# mod_producto(3, "Modificado", 100)


def delete_producto(id):
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conexion.commit()
    print(f"{cursor.rowcount} registros borrados")


# delete_producto(3)


def ver_productos():
    productos = cursor.execute("SELECT * FROM productos").fetchall()
    for p in productos:
        print(f"Id: {p.id}, nombre: {p.nombre}, precio: {p.precio: .2f}")


ver_productos()


def ver_producto(id):
    p = cursor.execute("SELECT * FROM productos WHERE id = ?", (id,)).fetchone()
    print(f"Id: {p.id}, nombre: {p.nombre}, precio: {p.precio: .2f}")

# ver_producto(1)

conexion.close()
