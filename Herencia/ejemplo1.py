class Empleado: # No usaremos propiedades (@property) para simplificar
    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

    def sube_sueldo(self, porcentaje):
        self.sueldo *= 1 + porcentaje/100
        
    @property
    def sueldo_mensual(self):
        return self.sueldo / 12
        
class Programador(Empleado): # Programador es un empleado
    def __init__(self, nombre, sueldo, lenguaje) -> None:
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje
    
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

programador = Programador("Megacrack", 50000, 'Python')
programador.sube_sueldo(10) # Llamo al método sobrescrito
print(f"{programador.nombre} - {programador.sueldo: .2f}")
print(programador.sueldo_mensual)

empleado = Empleado("Alguien", 50000)
empleado.sube_sueldo(10)
print(f"{empleado.nombre} - {empleado.sueldo: .2f}")
