class Empleado:
    sueldo_minimo = 14000 # atributo de clase (valor fuera del constructor)

    def __init__(self, nombre: str, sueldo: float) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

empleado = Empleado("Pepito", 16000)
empleado2 = Empleado("Juana", 32000)

Empleado.sueldo_minimo = 16000
print(empleado.sueldo_minimo) 
print(empleado.__dict__)
print(empleado2.sueldo_minimo) 
print(empleado2.__dict__)
print(Empleado.sueldo_minimo)
print(Empleado.__dict__)
