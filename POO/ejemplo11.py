# Métodos estáticos
class Empleado:
    sueldo_minimo = 14000 # atributo de clase

    @staticmethod
    def crea_becario(nombre):
        return Empleado(nombre, Empleado.sueldo_minimo)

    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

 # Resto de métodos

e = Empleado.crea_becario("Juanito")
print(e.sueldo) # 14000