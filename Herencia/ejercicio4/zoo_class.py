from animal_class import Animal
from mamifero_class import Mamifero
from ave_class import Ave

class Zoo:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__animales: list[Animal] = []
        
    def add_animales(self, *animales: Animal):
        self.__animales.extend(animales)
        
    def print_animales(self):
        for a in self.__animales:
            print(f"nombre: {a.nombre}, peso: {a.peso}.")
            if isinstance(a, Mamifero):
                print(f" - Mamifero {'carnivoro' if a.carnivoro else 'herbívoro'}")
            elif isinstance(a, Ave):
                print(f" - Ave {'que vuela' if a.volar else 'que no vuela'}")
        
    @property        
    def num_animales(self):
        return len(self.__animales)
    
    def get_cantidad(self, tipo: str):
        return len([a for a in self.__animales if a.tipo_animal() == tipo])
            