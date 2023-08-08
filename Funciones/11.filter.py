numeros = (3 ,5 ,12, 5, 9, 11, 10, 2)

# Lista con los números pares de la original (forma clásica - bucle)
pares = []
for n in numeros:
    if n % 2 == 0: # par
        pares.append(n)
        
print(pares)

# Igual pero con filter()
paresFilter = list(filter(lambda n: n % 2 == 0, numeros))
print(paresFilter)

# Igual pero con listas de comprensión (comprehension lists)
paresComList = [n for n in numeros if n % 2 == 0]
print(paresComList)
