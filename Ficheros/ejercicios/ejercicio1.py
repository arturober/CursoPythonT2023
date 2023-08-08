'''
Crea un archivo numeros.txt que contenga un número en cada línea
Desde Python, lee el contenido del archivo e imprime la suma de los números
'''
with open("Ficheros/archivos/numeros.txt") as f:
    numeros = [int(linea) for linea in f]
    print(f"La suma de {numeros} es: {sum(numeros)}")
    
# Foma tradicional
with open("Ficheros/archivos/numeros.txt") as f:
    total = 0
    for linea in f:
        total += int(linea)
        
    print(f"La suma es: {total}")
