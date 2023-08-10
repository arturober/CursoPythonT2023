from dataclasses import dataclass

@dataclass()
class Direccion:
    calle: str
    numero: int
    cp: str

d = Direccion("Calle de prueba", 32, "23423") 
print(d) # Direccion(calle='Calle de prueba', numero=32, cp='23423') 

@dataclass
class Persona:
    nombre: str
    edad: int
    direcciones: Direccion
    
p = Persona("Pepito", 34, d)
print(p) # Persona(nombre='Pepito', edad=34, direccion=Direccion(calle='Calle de prueba', numero=32, cp='23423'))
