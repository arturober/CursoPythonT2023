from abc import ABC, abstractmethod
import math

# Clase abstracta
class Figura(ABC):
    @abstractmethod # Método abstracto
    def get_area(self): 
        pass
    
    @abstractmethod # Método abstracto
    def get_perimetro(self): 
        pass
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def get_area(self):
        return math.pi * self.radio ** 2
    
    def get_perimetro(self):
        return math.pi * self.radio * 2
    
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def get_area(self):
        return self.ancho * self.alto
    
    def get_perimetro(self):
        return 2 * (self.ancho + self.alto)
    
# f = Figura() # TypeError: Can't instantiate abstract class Figura with abstract methods get_area, get_perimetro

c = Circulo(3)
print(c.get_area())
print(c.get_perimetro())