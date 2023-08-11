from abc import ABC, abstractclassmethod

class Animal(ABC):
    def __init__(self, nombre, peso) -> None:
        self.nombre = nombre
        self.peso = peso
        
    def comer(self):
        self.peso *= 1.05
        
    def __repr__(self) -> str:
        return f"{self.nombre} - {self.peso}"
    
    @abstractclassmethod 
    def tipo_animal(self):
        pass