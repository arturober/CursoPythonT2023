from animal_class import Animal

class Ave(Animal):
    def __init__(self, nombre, peso, volar) -> None:
        super().__init__(nombre, peso)
        self.volar = volar
        
    def __repr__(self) -> str:
        return super().__repr__() + (". Vuela" if self.volar else ". No vuela")