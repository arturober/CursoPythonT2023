'''
Crea la clase Rectangulo
Un rectángulo tiene como atributos ancho y alto
Crea los métodos para calcular el área y el perímetro del rectángulo

Crea un objeto de la clase y pruébalo
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
    
r = Rectangulo(4, 7)
print(r.__dict__)
print(f"Área: {r.area()}. Perímetro: {r.perimetro()}")
