def suma(n1: int, n2: int) -> int:
    return n1 + n2

print(suma(3, 4))

# Añadir el valor en mayúsculas a la lista
def add_lista(valor: str, lista: list[str]):
    lista.append(valor.upper())

lista = ["CASA", "COCHE"]
add_lista("MESA", lista)
print(lista)

def veces(lista: tuple[str], palabra: str) -> int:
    veces = 0
    for p in lista:
        if p == palabra:
            veces += 1
    return veces

palabras = ("casa", "coche", "moto", "casa", "árbol", "casa")
print(f"casa aparece {veces(palabras, 'casa')} veces") # casa aparece 3 veces
