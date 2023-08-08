'''
A partir del archivo notas.txt muestra lo siguiente por cada línea:
Las notas leídas y la media

Usa la función linea.split(";") para generar una lista con las notas por separado
Cuidado: las notas serán strings, debes transformarlas a float
'''

with open("Ficheros/archivos/notas.csv") as f:
    for linea in f:
        notas = [float(nota) for nota in linea.split(";")]
        print(f"{notas}. Media: {sum(notas)/len(notas): .2f}")
        
import csv
with open('Ficheros/archivos/notas.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for fila in reader:
        notas = [float(nota) for nota in fila]
        print(f"{notas}. Media: {sum(notas)/len(notas): .2f}")
        