# Atributos de clase con @dataclass
from dataclasses import dataclass

@dataclass
class Empleado:
    sueldo_minimo = 14000 # atributo de clase  (no se pueden tipar en dataclasses!)
    nombre: str
    sueldo: float

empleado = Empleado("Pepito", 16000)
empleado2 = Empleado("Juana", 32000)

Empleado.sueldo_minimo = 16000
print(empleado.sueldo_minimo) 
print(empleado.__dict__)
print(empleado2.sueldo_minimo) 
print(empleado2.__dict__)
print(Empleado.sueldo_minimo)

