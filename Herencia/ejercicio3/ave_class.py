from animal_class import Animal
import random

class Ave(Animal):
    def __init__(self, nombre, peso, volar) -> None:
        super().__init__(nombre, peso)
        self.volar = volar
        
    def __repr__(self) -> str:
        return super().__repr__() + (". Vuela" if self.volar else ". No vuela")
    
    def poner_huevos(self):
        huevos = random.randint(1, 6)
        self.peso -= huevos * 0.05
        print(f"He puesto {huevos} huevos")
        
    def tipo_animal(self):
        return "Ave"