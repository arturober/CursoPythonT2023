# Métodos especiales

class Cuadrado:
    # Constructor
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def area(self) -> int:
        return self.lado**2

    # Representa el objeto como string (se llama automaticamente al convertir el objeto a string)
    def __repr__(self) -> str: # Equivale a __str__ pero vale para todo
        return f"Cuadrado: {self.lado}"
    
    # Metodo que implementa el operador '+' entre cuadrados
    def __add__(self, other):
        return Cuadrado(self.lado + other.lado)
    
    # Método que implementa el operador '<' para comparar cuadrados (y poder ordenarlos)  
    def __lt__(self, other):
        return self.lado < other.lado  
    
c = Cuadrado(6)
print(c)
print(c.__repr__()) # Se puede llamar, pero es innecesario

c2 = Cuadrado(4)
c3 = c + c2
print(c3)

lista = [Cuadrado(4), Cuadrado(12), Cuadrado(10), Cuadrado(5), Cuadrado(2)]
print(lista)
# Para ordenar por defecto hay que implementar el operador '<' (__lt__)
lista.sort()
print(lista)

