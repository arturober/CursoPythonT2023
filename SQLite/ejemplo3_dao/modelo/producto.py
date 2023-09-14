from dataclasses import dataclass

@dataclass
class Producto:
    id: int
    nombre: str
    precio: float

    @staticmethod # Cuando el producto no tiene id (no insertado)
    def crea_nuevo(nombre, precio):
        return Producto(0, nombre, precio)