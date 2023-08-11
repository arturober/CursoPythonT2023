from animal_class import Animal


class Mamifero(Animal):
    def __init__(self, nombre, peso, carnivoro) -> None:
        super().__init__(nombre, peso)
        self.carnivoro = carnivoro
        
    def comer(self):
        super().comer()
        print(f"He comido {'carne' if self.carnivoro else 'hierba'}")
        
    def __repr__(self) -> str:
        return super().__repr__() + (". Carnívoro" if self.carnivoro else ". Herbívoro")