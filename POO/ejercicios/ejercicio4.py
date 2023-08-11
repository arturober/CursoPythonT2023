'''
Ejercicio de dataclass:
Crea la clase Empleado con los atributos nombre, edad y sueldo
Crea la clase Empresa con el atributo nombre y empleados -> list[Empleado]
Dentro de la empresa crea un método que devuelva el total de sueldos a pagar de todos los empleados
'''

from dataclasses import dataclass
import pprint

@dataclass
class Empleado:
    nombre: str
    edad: int
    sueldo: float

@dataclass
class Empresa:
    nombre: str
    empleados: list[Empleado]
    
    @property
    def total_sueldos(self):
        return sum(e.sueldo for e in self.empleados)
    
e = Empresa("Currantes SL", [
    Empleado("Juan", 45, 21000),
    Empleado("Sara", 24, 17000),
    Empleado("María", 60, 56000),
    Empleado("Paco", 39, 28000)
])

pprint.pprint(e)
print(f"Total sueldos: {e.total_sueldos}")