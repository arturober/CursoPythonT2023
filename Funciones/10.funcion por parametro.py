from collections.abc import Callable

def sumar(n1: int, n2: int) -> int:
    return n1 + n2

restar = lambda n1, n2: n1 - n2

# Callable[[int, int], int] equivale a función(int, int) -> int
def operar(operacion: Callable[[int, int], int], n1: int, n2: int) -> int:
    return operacion(n1, n2)

print(operar(sumar, 3, 5)) # 8
print(operar(restar, 3, 5)) # -2 
print(operar(lambda n1, n2: n1 * n2, 6, 7)) # 42

# --------------------------------------------------

palabras = ["casa", "pelota", "acera", "mesa", "zoo", "barbacoa"]
palabras.sort() # ordena alfabéticamente
print(palabras) # ['acera', 'casa', 'mesa', 'pelota', 'zoobarbacoa']

# Ordena la lista de palabras por longitud de la cadena
palabras.sort(key = lambda p: len(p)) # Ordenar palabras por su longitud
print(palabras)

