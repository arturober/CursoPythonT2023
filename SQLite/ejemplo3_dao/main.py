import sqlite3
from dao.producto_dao import ProductoDAO
from modelo.producto import Producto

database = sqlite3.connect("SQLite/productos.sqlite")

productoDAO = ProductoDAO(database)

# p = Producto.crea_nuevo("Altavoz", 100)
# productoDAO.insert(p)
# print(p)

productos = productoDAO.getAll()
for p in productos:
    print(p)
