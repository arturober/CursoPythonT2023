numeros = (3 ,5 ,12, 5, 9, 11, 10, 2)

# Genera una nueva lista con los elementos de la original multiplicados por 2
numeros2 = []
for n in numeros:
    numeros2.append(n*2)
    
print(numeros2)

# Lo mismo con la función map
numeros2Map = list(map(lambda n: n * 2, numeros))
print(numeros2Map)

# Lo mismo con listas de comprensión
numeros2ComLis = [n * 2 for n in numeros]
print(numeros2ComLis)

# Crea una lista con los nuḿeros pares de la original dividos entre 2
resultado = []
for n in numeros:
    if n % 2 == 0: # par
        resultado.append(n/2)
        
print(resultado)

# Lo mismo con filter y map
resultado2 = list(map(lambda n: n / 2, filter(lambda n: n % 2 == 0, numeros)))
print(resultado)

# Lo mismo con listas de comprensión
resultado3 = [n/2 for n in numeros if n % 2 == 0]
print(resultado3)

# Genera una lista que contenga las longitudes de las siguientes palabras [4, 3, 7, 10, 5]
palabras = ["casa", "aro", "cebolla", "murciélago", "coche"]
longitudes = [len(p) for p in palabras]

print(longitudes)

# Genera la misma lista que antes, pero solo de las palabras que empiezan por 'c' -> [4, 7, 5]
longitudes2 = [len(p) for p in palabras if p.startswith("c")]

print(longitudes2)