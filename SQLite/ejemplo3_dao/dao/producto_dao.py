from dataclasses import dataclass
from sqlite3 import Connection
from modelo.producto import Producto

@dataclass
class ProductoDAO:
    database: Connection
    
    @staticmethod
    def product_factory(cursor, row):
        return Producto(row[0], row[1], row[2])

    def getAll(self) -> list[Producto]:
        self.database.row_factory = self.product_factory
        cursor = self.database.cursor()
        return cursor.execute("SELECT * FROM productos").fetchall()

    def getOne(self, id: int) -> Producto:
        self.database.row_factory = self.product_factory
        cursor = self.database.cursor()
        return cursor.execute("SELECT * FROM productos WHERE id = ?", (id, )).fetchone()

    def insert(self, p: Producto) -> None:
        with self.database: # Autocommit
            cursor = self.database.cursor()
            cursor.execute("INSERT INTO productos(nombre, precio) VALUES(?, ?)", (p.nombre, p.precio))
            p.id = cursor.lastrowid