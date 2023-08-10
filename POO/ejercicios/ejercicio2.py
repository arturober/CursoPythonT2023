'''
A la clase Rectangulo añadele (y prueba):
- Un método para imprimir el rectángulo como string (imprime alto, ancho y área)
- Un método para sumar Rectángulos (suma los anchos y los altos)
- Un método para comparar si un rectángulo es menor que otro (usa el área)
    * PAra probar esto crea una lista de rectángulos y ordénala
'''

class Rectangulo:
    # Constructor
    def __init__(self, ancho: int, alto: int) -> None:
        self.ancho = ancho
        self.alto = alto
        
    def area(self) -> int:
        return self.ancho * self.alto
    
    def perimetro(self) -> int:
        return self.ancho*2 + self.alto*2
    
    def __repr__(self) -> str:
        return f"Rectángulo (ancho: {self.ancho}, alto: {self.alto}, área: {self.area()})"
    
    def __add__(self, other):
        return Rectangulo(self.ancho + other.ancho, self.alto + other.alto)
    
    def __lt__(self, other):
        return self.area() < other.area()
    
r = Rectangulo(4, 7)
r2 = Rectangulo(6, 10)
print(r)
r3 = r + r2
print(r3)

lista = [r3, r2, r]
lista.sort()
print(lista)
