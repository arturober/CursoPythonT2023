class Direccion:
    def __init__(self, calle: str, numero: int, cp: str) -> None:
        self.calle = calle
        self.numero = numero
        self.cp = cp

    def __repr__(self) -> str:
        return f"{self.calle} - {self.numero} ({self.cp})"

class Persona:
    def __init__(self, nombre: str, edad: int, direccion: Direccion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion # Agregación (objeto Dirección depende de Persona)
        
    def __repr__(self) -> str:
        return f"Nombre: {self.nombre}. Edad: {self.edad}. Direccion: {self.direccion}"

        
p = Persona("José", 54, Direccion("Calle perdida", 24, "24324"))
print(p) # Nombre: José. Edad: 54. Direccion: Calle perdida - 24 (24324)
print("Calle: " + p.direccion.calle)

