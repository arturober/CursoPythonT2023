class Cuadrado:
    # Constructor
    def __init__(self, lado: int) -> None:
        self.__lado = lado # lado es privado (no se debe acceder desde fuera de la clase)

    def area(self) -> int:
        return self.__lado**2

    # Representa el objeto como string (se llama automaticamente al convertir el objeto a string)
    def __repr__(self) -> str: # Equivale a __str__ pero vale para todo
        return f"Cuadrado: {self.__lado}"
    
c = Cuadrado(5)
# print(c.__lado) # AttributeError: 'Cuadrado' object has no attribute '__lado'
print(c._Cuadrado__lado) # 5 -> Name Manglin: Se supone que no debemos acceder así
print(c.area())
print(c)
