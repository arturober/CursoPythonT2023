from ave_class import Ave
from mamifero_class import Mamifero
from zoo_class import Zoo


m = Mamifero("León", 200, True)
m.comer()
print(m)
print(m.tipo_animal())

a = Ave("Avestruz", 50, False)
a.comer()
a.poner_huevos()
print(a)
print(a.tipo_animal())

zoo = Zoo("Animalandia")
zoo.add_animales(
    m,
    a,
    Mamifero("Hiena", 40, True),
    Ave("loro", 1.2, True),
    Mamifero("gacela", 75, False)
)

zoo.print_animales()

print(f"Total animales: {zoo.num_animales}")
print(f"Total mamíferos: {zoo.get_cantidad('Mamífero')}")
print(f"Total aves: {zoo.get_cantidad('Ave')}")

