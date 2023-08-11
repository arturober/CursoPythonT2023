from ave_class import Ave
from mamifero_class import Mamifero
from animal_class import Animal

m = Mamifero("León", 200, True)
m.comer()
print(m)
print(m.tipo_animal())

a = Ave("Avestruz", 50, False)
a.comer()
a.poner_huevos()
print(a)
print(a.tipo_animal())

