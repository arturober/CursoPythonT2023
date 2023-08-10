class Cuadrado:
    # Constructor
    def __init__(self, lado: int) -> None:
        self.lado = lado
        
    def area(self) -> int:
        return self.lado ** 2
        
    
c = Cuadrado(6) # lado = 6
print(c.lado)

c2 = Cuadrado(12)
print(c2.lado)
c2.lado = 100
print(c2.lado)

print(c.area()) # 36
print(c2.area()) # 10000


