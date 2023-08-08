try:
    with open("Ficheros/archivos/a2.txt") as f:
        for linea in f:
            print(linea.strip())
except FileNotFoundError as e:
    print(f"Archivo no encontrado: {e}")
except Exception as e:
    print(f"Error: {e}")

        
print("Sigo con el programa")

lista = []
try:
    media = sum(lista)/len(lista)
except ZeroDivisionError:
    print("División entre cero")
    
# Como lanzar errores en nuestras funciones
def caracter_mayus(cadena: str, pos: int):
    if pos < 0 or pos >= len(cadena):
        raise IndexError(f"La posición no es correcta. Debe estar entre 0 y {len(cadena) - 1}")
    return cadena[pos].upper()

print(caracter_mayus("Hola", 2))
print(caracter_mayus("Hola", 5))

