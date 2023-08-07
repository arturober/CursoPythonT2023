def mod_num(n):
    n = 100
    print(f"Función: {n}")
    
n = 1
mod_num(n) # Función: 100
print(f"Main: {n}") # Main: 1. La modificación no tiene efecto fuera

def mod_lista(lista):
    lista[0] = 99
    print(f"Función: {lista}") # [99, 2, 3, 4]

lista = [1, 2, 3, 4]
mod_lista(lista)
print(f"Main: {lista}") # [99, 2, 3, 4] Modificada! 

