# Métodos de clase
class Empleado:
    sueldo_minimo = 14000 # atributo de clase

    @classmethod
    def crea_becario(cls, nombre):
        return cls(nombre, cls.sueldo_minimo)

    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

 # Resto de métodos

e = Empleado.crea_becario("Juanito")
print(e.sueldo) # 14000