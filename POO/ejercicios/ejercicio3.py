'''
Crea la clase Producto con los atributos privados nombre y precio
El nombre será de solo lectura y el precio de lectura/escritura y no admite valores negativos (usa propiedades)
Crea otra propiedad llamada precio_iva que devuelva el precio con un 21% extra
Crea también el método __repr__ para imprimir el producto
'''

class Producto:
    def __init__(self, nombre, precio) -> None:
        self.__nombre = nombre
        self.precio = precio
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        if precio < 0:
            raise AttributeError(f"El precio no puede ser negativo: {precio}")
        self.__precio = precio
        
    @property
    def precio_iva(self):
        return self.precio * 1.21
    
    def __repr__(self) -> str:
        return f"Producto (nombre: {self.nombre}, precio: {self.precio})"
    
p = Producto("Ordenador", 500)
print(p)
p.precio = 600
#p.nombre = "Hola" # AttributeError: can't set attribute 'nombre'
print(p.precio, p.precio_iva)