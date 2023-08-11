# Ejemplo 1 con @dataclass

from dataclasses import dataclass

@dataclass
class Empleado: # No usaremos propiedades (@property) para simplificar
    nombre: str
    sueldo: float

    def sube_sueldo(self, porcentaje):
        self.sueldo *= 1 + porcentaje/100
        
    @property
    def sueldo_mensual(self):
        return self.sueldo / 12
        
@dataclass
class Programador(Empleado): # Programador es un empleado
    lenguaje: str
    
    # Sobrescribir método sube_sueldo
    def sube_sueldo(self, porcentaje):
        super().sube_sueldo(porcentaje) # Ejecutamos método original (heredado)
        if self.lenguaje == 'Python': # Añadimos funcionalidad extra
            print("El programador de Python sube un 5% extra")
            self.sueldo *= 1.05
            
    #Sobrescritura de propiedades
    @property
    def sueldo_mensual(self):
        sueldo = super().sueldo_mensual
        return sueldo + 100 if self.lenguaje == "Python" else sueldo
    
programador = Programador("Pepito", 20000, 'Python')
print(programador)

print(issubclass(Programador, object)) # True (Programador hereda de object)
print(issubclass(Programador, Empleado)) # True
print(issubclass(Empleado, Programador)) # False
print(isinstance(programador, object)) # True (p es un objeto)
print(isinstance(programador, Empleado)) # True (p es un Empleado)
print(isinstance(programador, Programador)) # True (p es un Programador)
