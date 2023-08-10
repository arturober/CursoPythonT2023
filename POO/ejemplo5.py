class Cuadrado:
    # Constructor
    def __init__(self, lado: int) -> None:
        self.lado = lado # Llamamos al setter desde el constructor 

    @property # Getter de la propiedad lado (__lado)
    def lado(self) -> int:
        return self.__lado
    
    @lado.setter # Setter de la propiedad lado
    def lado(self, lado: int):
        if not isinstance(lado, int) or lado < 0:
            raise AttributeError("El lado debe ser un entero positivo")
        self.__lado = lado # lado es privado (no se debe acceder desde fuera de la clase)
    
    @property
    def area(self) -> int:
        return self.__lado**2

    # Representa el objeto como string (se llama automaticamente al convertir el objeto a string)
    def __repr__(self) -> str: # Equivale a __str__ pero vale para todo
        return f"Cuadrado: {self.__lado}"
    
c = Cuadrado(5)
# c.lado = -36 # AttributeError: El lado debe ser un entero positivo
c.lado = 6
print(c.lado)
print(c.area)


