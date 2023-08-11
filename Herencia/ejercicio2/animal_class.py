class Animal:
    def __init__(self, nombre, peso) -> None:
        self.nombre = nombre
        self.peso = peso
        
    def comer(self):
        self.peso *= 1.05
        
    def __repr__(self) -> str:
        return f"{self.nombre} - {self.peso}"